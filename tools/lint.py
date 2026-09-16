#!/usr/bin/env python3
"""Style and rendering linter for the cphb-rs mdBook sources.

Catches the class of defect that `mdbook build` reports success on but that
renders as garbage in the browser -- most importantly a TikZ picture that was
never wrapped in a <script type="text/tikz"> tag.

Usage:  python3 tools/lint.py [src_dir]
Exit code 1 if any problem is found.
"""

import os
import re
import sys

# Fence info-strings we consider valid.
VALID_FENCES = {
    "", "rust", "rust, ignore", "rust, compile_fail", "rust, no_run",
    "dot process", "text", "sh", "bash", "cpp", "ignore",
}

# LaTeX macros that must never survive into prose.
PROSE_MACROS = re.compile(r"\\(?:key|emph|texttt|textbf|textit|footnote|index|"
                          r"section|subsection|chapter|item|lstinline)\b")

# CommonMark eats a backslash before ASCII punctuation, so `\{` reaches
# MathJax as a bare `{` and the braces vanish. Inside math such a backslash
# must be doubled. A backslash before a letter (\sum, \texttt) is untouched
# by Markdown and is correct either way.
# An odd-length run of backslashes before punctuation loses one to Markdown;
# an even-length run survives as half its length, which is what we want.
PUNCT = set("!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~")
ESCAPE = re.compile(r"(\\+)([^A-Za-z\s\\])")
INLINE_MATH = re.compile(r"(?<!\$)\$([^$\n]+)\$(?!\$)")

TIKZ_OPEN = re.compile(r'<script\s+type="text/tikz">')
TIKZ_CLOSE = re.compile(r"</script>")


def strip_math(line):
    """Remove math spans so macros inside them are not flagged."""
    line = re.sub(r"\\\\\[.*?\\\\\]", " ", line)
    line = re.sub(r"\\\\\(.*?\\\\\)", " ", line)
    line = re.sub(r"\$\$.*?\$\$", " ", line)
    line = re.sub(r"\$[^$]*\$", " ", line)
    line = re.sub(r"`[^`]*`", " ", line)
    return line


def lint_file(path):
    problems = []
    rel = os.path.basename(path)
    with open(path, encoding="utf-8") as fh:
        lines = fh.read().split("\n")

    # A NUL byte means tex2md.py left a masking sentinel behind. Markdown
    # renders it invisibly and grep treats the file as binary, so it hides.
    for n, line in enumerate(lines, 1):
        if "\x00" in line:
            problems.append((n, "sentinel",
                             "NUL byte: an unreplaced tex2md masking sentinel"))

    in_tikz = False
    tikz_start = 0
    in_code = False
    in_display = False

    for n, line in enumerate(lines, 1):
        stripped = line.strip()

        # --- fenced code blocks -------------------------------------------
        if stripped.startswith("```"):
            info = stripped[3:].strip()
            if not in_code:
                in_code = True
                if info not in VALID_FENCES:
                    problems.append((n, "fence", f"unknown fence info-string: ```{info}"))
            else:
                in_code = False
            continue
        if in_code:
            continue

        # --- tikz script tracking ------------------------------------------
        if TIKZ_OPEN.search(line):
            if in_tikz:
                problems.append((n, "tikz", "nested <script type=\"text/tikz\">"))
            in_tikz, tikz_start = True, n
            continue
        if in_tikz and TIKZ_CLOSE.search(line):
            in_tikz = False
            continue

        if stripped.startswith("\\begin{tikzpicture}") and not in_tikz:
            problems.append((n, "tikz",
                             "\\begin{tikzpicture} not wrapped in "
                             "<script type=\"text/tikz\"> -- renders as literal LaTeX"))

        if in_tikz:
            continue  # TikZ bodies are LaTeX; nothing below applies

        # --- display-math row breaks ----------------------------------------
        # Markdown collapses \\ to \ before MathJax sees it, so a LaTeX row
        # break must be written with four backslashes. Two collapse to a lone
        # backslash and break the surrounding cases/array environment.
        # Single backslashes before letters (\texttt, \sum) pass through
        # untouched and are fine either way.
        if "\\\\[" in line or re.search(r"\\+begin\{(equation\*?|align\*?|gather\*?)\}", line):
            in_display = True
        if in_display:
            # A line holding only an operator is invisible to LaTeX but not
            # to Markdown: a lone "=" or "-" is a setext heading underline
            # and splits the display block in two.
            if stripped and re.fullmatch(r"[=+\-*/<>~.,;:|]+", stripped):
                problems.append((n, "math",
                                 f"line holding only `{stripped}` inside display math: "
                                 "Markdown reads it as a heading/bullet and splits the "
                                 "block (join it to the next line)"))
            m = re.search(r"(\\+)\s*$", line)
            if m and len(m.group(1)) % 4 != 0:
                problems.append((n, "math",
                                 f"trailing run of {len(m.group(1))} backslashes in display "
                                 "math; a row break must be written as four"))
            if "\\\\]" in line or re.search(r"\\+end\{(equation\*?|align\*?|gather\*?)\}", line):
                in_display = False
            continue  # macros inside display math are MathJax's problem, not ours

        # --- backslash-before-punctuation inside inline math ----------------
        for span in INLINE_MATH.finditer(line):
            for esc in ESCAPE.finditer(span.group(1)):
                run, char = esc.group(1), esc.group(2)
                if len(run) % 2 == 1 and char in PUNCT:
                    problems.append((n, "escape",
                                     f"`{run}{char}` in inline math: Markdown eats the "
                                     "backslash, so MathJax never sees it (double it)"))

        # --- stray LaTeX in prose ------------------------------------------
        if stripped.startswith("%"):
            problems.append((n, "latex", "LaTeX comment line renders as visible text"))

        prose = strip_math(line)
        m = PROSE_MACROS.search(prose)
        if m:
            problems.append((n, "latex", f"LaTeX macro {m.group(0)} in prose"))

    if in_tikz:
        problems.append((tikz_start, "tikz", "unclosed <script type=\"text/tikz\">"))
    if in_code:
        problems.append((len(lines), "fence", "unclosed code fence"))

    return [(rel, n, kind, msg) for n, kind, msg in problems]


def lint_summary(src):
    """SUMMARY.md hygiene: link titles, dangling links, orphaned files."""
    problems = []
    path = os.path.join(src, "SUMMARY.md")
    with open(path, encoding="utf-8") as fh:
        lines = fh.read().split("\n")

    linked = set()
    for n, line in enumerate(lines, 1):
        if line.strip().startswith("<!--"):
            continue  # intentionally deferred chapters
        for title, target in re.findall(r"\[([^\]]*)\]\(([^)]+)\)", line):
            if title != title.strip():
                problems.append(("SUMMARY.md", n, "summary",
                                 f"link title has surrounding whitespace: [{title}]"))
            linked.add(target)
            if not os.path.exists(os.path.join(src, target)):
                problems.append(("SUMMARY.md", n, "summary",
                                 f"link target does not exist: {target}"))

    on_disk = {f for f in os.listdir(src)
               if f.endswith(".md") and not f.startswith(".")}
    for orphan in sorted(on_disk - linked - {"SUMMARY.md", "README.md"}):
        problems.append(("SUMMARY.md", 0, "summary",
                         f"file in src/ not referenced by SUMMARY: {orphan}"))
    return problems


def main():
    src = sys.argv[1] if len(sys.argv) > 1 else "src"
    problems = []
    for name in sorted(os.listdir(src)):
        if name.startswith("._") or name.startswith("."):
            continue  # macOS AppleDouble sidecars on exFAT volumes
        if name.endswith(".md") and name != "SUMMARY.md":
            problems += lint_file(os.path.join(src, name))
    problems += lint_summary(src)

    if not problems:
        print("lint: clean")
        return 0

    by_kind = {}
    for rel, n, kind, msg in problems:
        by_kind.setdefault(kind, []).append((rel, n, msg))
    for kind in sorted(by_kind):
        print(f"\n== {kind} ({len(by_kind[kind])}) ==")
        for rel, n, msg in by_kind[kind]:
            print(f"  {rel}:{n}: {msg}")
    print(f"\nlint: {len(problems)} problem(s)")
    return 1


if __name__ == "__main__":
    sys.exit(main())
