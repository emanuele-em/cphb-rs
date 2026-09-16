#!/usr/bin/env python3
"""Expand \\newcommand macros inside <script type="text/tikz"> blocks.

TikZJax runs a real but minimal TeX, and the upstream book defines local
\\newcommand helpers that sometimes use \\ifthenelse -- which needs the
ifthen package that TikZJax does not ship. Rather than gamble on what the
browser-side engine supports, we inline the macros so every picture is
plain TikZ.

    python3 tools/expand_tikz_macros.py file.md [file.md ...]
"""

import re
import sys


def brace_arg(text, i):
    assert text[i] == "{"
    depth, j = 0, i
    while j < len(text):
        if text[j] == "{":
            depth += 1
        elif text[j] == "}":
            depth -= 1
            if depth == 0:
                return text[i + 1:j], j + 1
        j += 1
    raise ValueError("unbalanced brace")


def parse_defs(block):
    """Pull out \\newcommand\\name[n]{body}; return (defs, block_without_defs)."""
    defs = {}
    out, i = [], 0
    pat = re.compile(r"\\newcommand\\([A-Za-z]+)\[(\d+)\]\s*")
    while True:
        m = pat.search(block, i)
        if not m:
            out.append(block[i:])
            break
        body, after = brace_arg(block, m.end())
        defs[m.group(1)] = (int(m.group(2)), body)
        out.append(block[i:m.start()])
        i = after
    return defs, "".join(out)


def resolve_ifthen(text):
    """\\ifthenelse{\\equal{A}{B}}{yes}{no} with literal A/B."""
    while True:
        k = text.find("\\ifthenelse")
        if k == -1:
            return text
        cond, i = brace_arg(text, k + len("\\ifthenelse"))
        yes, i = brace_arg(text, i)
        no, i = brace_arg(text, i)
        m = re.fullmatch(r"\s*\\equal\{([^{}]*)\}\{([^{}]*)\}\s*", cond)
        if not m:
            raise ValueError(f"unsupported \\ifthenelse condition: {cond!r}")
        text = text[:k] + (yes if m.group(1).strip() == m.group(2).strip() else no) + text[i:]


def expand_once(text, defs):
    for name, (arity, body) in defs.items():
        pat = "\\" + name
        k = text.find(pat)
        while k != -1:
            end = k + len(pat)
            # must not be a longer macro name
            if end < len(text) and text[end].isalpha():
                k = text.find(pat, end)
                continue
            args, i = [], end
            try:
                for _ in range(arity):
                    while i < len(text) and text[i] in " \n":
                        i += 1
                    a, i = brace_arg(text, i)
                    args.append(a)
            except (AssertionError, ValueError, IndexError):
                k = text.find(pat, end)
                continue
            filled = body
            for n, a in enumerate(args, 1):
                filled = filled.replace(f"#{n}", a)
            text = text[:k] + filled + text[i:]
            return text, True
    return text, False


def process_block(block):
    defs, block = parse_defs(block)
    if not defs:
        return block, 0
    count = 0
    while True:
        block, changed = expand_once(block, defs)
        if not changed:
            break
        count += 1
        if count > 20000:
            raise RuntimeError("macro expansion did not terminate")
    block = resolve_ifthen(block)
    block = re.sub(r"\n{3,}", "\n\n", block)
    return block, len(defs)


def main():
    for path in sys.argv[1:]:
        text = open(path, encoding="utf-8").read()
        out, total = [], 0
        pos = 0
        for m in re.finditer(r'(<script type="text/tikz">)(.*?)(</script>)', text, re.S):
            body, n = process_block(m.group(2))
            total += n
            out.append(text[pos:m.start()])
            out.append(m.group(1) + body + m.group(3))
            pos = m.end()
        out.append(text[pos:])
        if total:
            open(path, "w", encoding="utf-8").write("".join(out))
        print(f"{path}: {total} macro definition(s) expanded")
    return 0


if __name__ == "__main__":
    sys.exit(main())
