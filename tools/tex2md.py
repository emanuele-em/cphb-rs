#!/usr/bin/env python3
"""Convert a chapter of the upstream CPHB LaTeX into this book's Markdown.

    python3 tools/tex2md.py chapter22.tex list.tex outdir/

Writes one file per \\section plus one chapter-intro file.

The conversion is deliberately conservative: it handles the mechanical
90% (structure, macros, math escaping, TikZ extraction, citations,
footnotes) and leaves anything needing judgement clearly marked. In
particular every C++ listing is emitted as a ```cpp block tagged
TODO-RUST, because the code must be rewritten from scratch, not
translated line by line.

Why the masking passes matter: a TikZ body legitimately contains
\\texttt{}, \\emph and $...$ that must survive untouched, so those regions
are replaced by sentinels before any prose rule runs.
"""

import os
import re
import sys

SENTINEL = "\x00{}{}\x00"
PUNCT = set("!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~")


# ----------------------------------------------------------------- utilities

def brace_arg(text, start):
    """Return (arg, index_after) for a {...} group starting at text[start]=='{'."""
    assert text[start] == "{"
    depth, i = 0, start
    while i < len(text):
        if text[i] == "{":
            depth += 1
        elif text[i] == "}":
            depth -= 1
            if depth == 0:
                return text[start + 1:i], i + 1
        i += 1
    raise ValueError("unbalanced brace")


def replace_cmd(text, name, render):
    """Replace every \\name{...} using render(arg), innermost-safe."""
    out, i, tag = [], 0, "\\" + name
    while True:
        j = text.find(tag, i)
        if j == -1 or j + len(tag) >= len(text):
            out.append(text[i:])
            break
        k = j + len(tag)
        if text[k] != "{":
            out.append(text[i:k])
            i = k
            continue
        arg, after = brace_arg(text, k)
        out.append(text[i:j])
        out.append(render(arg))
        i = after
    return "".join(out)


def double_all(s):
    """Double every backslash (display-math convention used by ch21)."""
    return s.replace("\\", "\\\\")


def double_punct(s):
    """Double only backslashes Markdown would eat (inline-math convention)."""
    return re.sub(r"(\\+)([^A-Za-z\s\\])",
                  lambda m: (m.group(1) * 2 if len(m.group(1)) % 2 else m.group(1)) + m.group(2)
                  if m.group(2) in PUNCT else m.group(0),
                  s)


# ------------------------------------------------------------------- masking

class Masker:
    def __init__(self):
        self.store = {}
        self.n = 0

    def put(self, kind, body):
        key = SENTINEL.format(kind, self.n)
        self.store[key] = (kind, body)
        self.n += 1
        return key


def mask_environments(text, m):
    # TikZ pictures (may be wrapped in \begin{center})
    def tikz(match):
        return m.put("T", match.group(0))
    text = re.sub(r"\\begin\{tikzpicture\}.*?\\end\{tikzpicture\}", tikz, text, flags=re.S)

    def listing(match):
        return m.put("L", match.group(1))
    text = re.sub(r"\\begin\{lstlisting\}(.*?)\\end\{lstlisting\}", listing, text, flags=re.S)

    # display math: \[ ... \] and equation/align/gather environments
    def disp(match):
        return m.put("D", match.group(0))
    text = re.sub(r"\\\[.*?\\\]", disp, text, flags=re.S)
    text = re.sub(r"\\begin\{(equation\*?|align\*?|gather\*?)\}.*?\\end\{\1\}",
                  disp, text, flags=re.S)

    def inline(match):
        return m.put("I", match.group(1))
    text = re.sub(r"(?<!\\)\$([^$\n]+)\$", inline, text)
    return text


def unmask(text, m):
    for key in sorted(m.store, key=lambda k: -len(k)):
        kind, body = m.store[key]
        if kind == "T":
            rendered = '<script type="text/tikz">\n' + body.strip() + "\n</script>"
        elif kind == "L":
            rendered = ("<!-- TODO-RUST: rewrite this listing in idiomatic Rust -->\n"
                        "```cpp\n" + body.strip("\n") + "\n```")
        elif kind == "D":
            inner = body.strip()
            if re.match(r"\\begin\{(equation|align|gather)", inner):
                # already a display environment; wrapping it in \[ \] would nest
                rendered = double_all(inner)
            else:
                if inner.startswith("\\["):
                    inner = inner[2:]
                if inner.endswith("\\]"):
                    inner = inner[:-2]
                rendered = "\\\\[\n" + double_all(inner.strip()) + "\n\\\\]"
        else:
            rendered = "$" + double_punct(body) + "$"
        text = text.replace(key, rendered)
    return text


# ------------------------------------------------------------------ prose

def convert_prose(text, cites, footnotes):
    # Drop commented-out lines with their newline. Leaving an empty line
    # behind would split the surrounding paragraph in two.
    text = re.sub(r"(?m)^[ \t]*%.*\n", "", text)
    # drop whole-line \index{...} entries with their newline, so they do not
    # leave a blank line that splits the surrounding paragraph in two
    text = re.sub(r"(?m)^[ \t]*\\index\{[^{}]*\}[ \t]*\n", "", text)
    text = replace_cmd(text, "index", lambda a: "")
    text = replace_cmd(text, "key", lambda a: f"**{a}**")
    text = replace_cmd(text, "textbf", lambda a: f"**{a}**")
    text = replace_cmd(text, "emph", lambda a: f"_{a}_")
    text = replace_cmd(text, "textit", lambda a: f"_{a}_")
    text = replace_cmd(text, "texttt", lambda a: f"`{a}`")
    text = replace_cmd(text, "subsubsection*", lambda a: f"\n## {a}\n")
    text = replace_cmd(text, "subsubsection", lambda a: f"\n## {a}\n")

    def footnote(arg):
        footnotes.append(arg.strip())
        return f"[^{len(footnotes)}]"
    text = replace_cmd(text, "footnote", footnote)

    def cite(arg):
        nums = [str(cites[k.strip()]) for k in arg.split(",") if k.strip() in cites]
        return "[" + ", ".join(nums) + "]" if nums else ""
    text = replace_cmd(text, "cite", cite)

    for env in ("center", "multicols", "itemize", "enumerate",
                "samepage", "sloppypar", "figure", "table"):
        text = re.sub(r"\\begin\{" + env + r"\}(\{[^}]*\})?", "", text)
        text = re.sub(r"\\end\{" + env + r"\}", "", text)
    text = re.sub(r"(?m)^\s*\\item\s+", "- ", text)

    text = text.replace("---", "\u2014").replace("--", "\u2013")
    text = text.replace("~", " ")
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


# ------------------------------------------------------------------- driver

def load_cites(path):
    keys = re.findall(r"\\bibitem\{([^}]+)\}", open(path, encoding="utf-8").read())
    return {k: i for i, k in enumerate(keys, 1)}


def slug(title):
    s = title.lower()
    s = s.replace("'", "").replace("\u2019", "")
    s = re.sub(r"[^a-z0-9]+", "_", s)
    return s.strip("_")


def convert_chunk(title, body, cites, level="#"):
    m = Masker()
    masked = mask_environments(body, m)
    footnotes = []
    prose = convert_prose(masked, cites, footnotes)
    out = unmask(prose, m)
    text = f"{level} {title}\n\n{out}\n"
    if footnotes:
        text += "\n___\n\n" + "\n\n".join(
            f"[^{i}]: {f}" for i, f in enumerate(footnotes, 1)) + "\n"
    return text


def main():
    if len(sys.argv) != 4:
        print(__doc__)
        return 2
    tex_path, list_path, outdir = sys.argv[1:4]
    tex = open(tex_path, encoding="utf-8").read()
    cites = load_cites(list_path)
    os.makedirs(outdir, exist_ok=True)

    cm = re.search(r"\\chapter\{([^}]+)\}", tex)
    chapter = cm.group(1)
    rest = tex[cm.end():]

    parts = re.split(r"\\section\{([^}]+)\}", rest)
    intro, sections = parts[0], list(zip(parts[1::2], parts[2::2]))

    written = []
    path = os.path.join(outdir, slug(chapter) + ".md")
    open(path, "w", encoding="utf-8").write(convert_chunk(chapter, intro, cites))
    written.append(path)
    for title, body in sections:
        path = os.path.join(outdir, slug(title) + ".md")
        open(path, "w", encoding="utf-8").write(convert_chunk(title, body, cites))
        written.append(path)

    for p in written:
        n = sum(1 for _ in open(p, encoding="utf-8"))
        print(f"  {p}  ({n} lines)")
    todo = sum(open(p, encoding="utf-8").read().count("TODO-RUST") for p in written)
    print(f"\n{len(written)} file(s); {todo} listing(s) need a Rust rewrite")
    return 0


if __name__ == "__main__":
    sys.exit(main())
