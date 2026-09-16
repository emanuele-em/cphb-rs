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


# A line holding nothing but an operator is invisible to LaTeX but not to
# Markdown: a lone "=" or "-" is a setext heading underline, and a lone "+"
# or "-" is a list bullet. The upstream book puts operators on their own
# line between matrices, which would silently split the display block and
# turn the preceding paragraph into a heading. Join them onto the next line
# -- whitespace inside math carries no meaning, so the LaTeX is unchanged.
OPERATOR_ONLY = re.compile(r"^[=+\-*/<>~.,;:|]+$")


def join_operator_lines(s):
    """Append operator-only lines to the PREVIOUS line.

    Prepending them to the next line instead would leave the line starting
    with "+ " or "- ", which Markdown reads as a list bullet -- trading one
    bug for another.
    """
    out = []
    for line in s.split("\n"):
        stripped = line.strip()
        if stripped and OPERATOR_ONLY.match(stripped) and out:
            out[-1] = out[-1].rstrip() + " " + stripped
        else:
            out.append(line)
    return "\n".join(out)


ALIGN = {"r": "---:", "l": ":---", "c": ":---:"}


def convert_tabular(text):
    """Turn \\begin{tabular} blocks into GitHub-flavoured Markdown tables."""

    def one(match):
        spec, body = match.group(1), match.group(2)
        # The book also uses tabular purely to sit figures side by side. A
        # GFM cell is single-line and cannot hold a <script> block, so drop
        # the scaffolding and let the figures stack instead.
        # Note the sentinel test: during a normal run the pictures have
        # already been masked, so the body holds "\x00T<n>\x00", not markup.
        if "<script" in body or "\x00T" in body or "\\begin{tikzpicture}" in body:
            body = body.replace("\\hline", "")
            def blank(cell):
                # spacer cells carry no content: \hspace{..}, \quad, \, ...
                c = re.sub(r"\\(?:hspace|vspace)\{[^}]*\}|\\q?quad|\\[,;:!]", "", cell)
                return not c.strip()

            rows = [[c.strip() for c in r.split("&")] for r in body.split("\\\\")]
            rows = [[c for c in r if not blank(c)] for r in rows]
            rows = [r for r in rows if r]

            def has_figure(row):
                return any("\x00T" in c or "<script" in c for c in row)

            out, i = [], 0
            while i < len(rows):
                row = rows[i]
                # a row of figures is often captioned by the step numbers on
                # the row below; pair them so the labels survive stacking
                if (has_figure(row) and i + 1 < len(rows)
                        and not has_figure(rows[i + 1])
                        and len(rows[i + 1]) == len(row)):
                    for fig, label in zip(row, rows[i + 1]):
                        out.append(fig)
                        out.append(f"_{label}_")
                    i += 2
                else:
                    out.extend(row)
                    i += 1
            return "\n\n" + "\n\n".join(out) + "\n\n"
        cols = [ALIGN.get(c, ":---") for c in spec if c in ALIGN]
        rows, rule_after = [], None
        for raw in body.split("\\\\"):
            if "\\hline" in raw:
                # remember where the rule fell, then drop it
                rule_after = len(rows)
                raw = raw.replace("\\hline", "")
            cells = [c.strip() for c in raw.split("&")]
            if any(cells):
                rows.append(cells)
        if not rows:
            return ""
        if not cols:
            cols = [":---"] * len(rows[0])
        # a rule straight after the first row marks it as a header;
        # otherwise the table has none and GFM still requires one
        if rule_after == 1:
            head, body_rows = rows[0], rows[1:]
        else:
            head, body_rows = [""] * len(cols), rows
        out = ["| " + " | ".join(head) + " |",
               "| " + " | ".join(cols) + " |"]
        out += ["| " + " | ".join(r) + " |" for r in body_rows]
        return "\n" + "\n".join(out) + "\n"

    return re.sub(r"\\begin\{tabular\}\{([^}]*)\}(.*?)\\end\{tabular\}",
                  one, text, flags=re.S)


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
            inner = join_operator_lines(body.strip())
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

    def cite(arg):
        nums = [str(cites[k.strip()]) for k in arg.split(",") if k.strip() in cites]
        return "[" + ", ".join(nums) + "]" if nums else ""
    text = replace_cmd(text, "cite", cite)

    text = convert_tabular(text)
    text = re.sub(r"(?m)^\\noindent\s*$\n?", "", text)

    for env in ("center", "multicols", "itemize", "enumerate",
                "samepage", "sloppypar", "figure", "table"):
        # also swallow optional arguments: \begin{itemize}[noitemsep]
        text = re.sub(r"\\begin\{" + env + r"\}(\[[^\]]*\])?(\{[^}]*\})?", "", text)
        text = re.sub(r"\\end\{" + env + r"\}", "", text)
    # \item, optionally carrying its own label: \item[(1)] keeps the "(1)"
    text = re.sub(r"(?m)^\s*\\item\[([^\]]*)\]\s*", r"- \1 ", text)
    text = re.sub(r"(?m)^\s*\\item\s+", "- ", text)

    text = text.replace("---", "\u2014").replace("--", "\u2013")
    text = text.replace("~", " ")

    # Extract footnotes LAST, so their bodies have already been through every
    # transform above while still part of the text. Pulling them out earlier
    # leaves \cite and masked-math sentinels unresolved inside the notes.
    def footnote(arg):
        footnotes.append(arg.strip())
        return f"[^{len(footnotes)}]"
    text = replace_cmd(text, "footnote", footnote)

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
    text = f"{level} {title}\n\n{prose}\n"
    if footnotes:
        text += "\n___\n\n" + "\n\n".join(
            f"[^{i}]: {f}" for i, f in enumerate(footnotes, 1)) + "\n"
    # unmask the assembled document, footnote bodies included -- they can
    # hold masked math of their own
    return unmask(text, m)


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

    leaked = [p for p in written if "\x00" in open(p, encoding="utf-8").read()]
    if leaked:
        print("ERROR: unreplaced masking sentinels left in: " + ", ".join(leaked))
        return 1

    for p in written:
        n = sum(1 for _ in open(p, encoding="utf-8"))
        print(f"  {p}  ({n} lines)")
    todo = sum(open(p, encoding="utf-8").read().count("TODO-RUST") for p in written)
    print(f"\n{len(written)} file(s); {todo} listing(s) need a Rust rewrite")
    return 0


if __name__ == "__main__":
    sys.exit(main())
