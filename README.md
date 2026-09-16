# cphb-rs
Competitive Programming Handbook - Rust Edition

## Local preview

Install [Graphviz](https://graphviz.org/download/) (`brew install graphviz`
on macOS or `sudo apt-get install graphviz` on Ubuntu), then install the
same build tools used by CI:

```sh
cargo install --locked --version 0.4.52 --root .tools mdbook
cargo install --locked --version 0.2.0 --root .tools mdbook-graphviz
export PATH="$PWD/.tools/bin:$PATH"
mdbook serve --hostname 127.0.0.1 --port 3000
```

Open <http://127.0.0.1:3000>. Use `mdbook build` for a static build in `book/`.
The book currently requires mdBook 0.4, not 0.5.

### Math and diagrams

MathJax is the only math renderer. The configuration in `theme/head.hbs`
supports `$...$` / `$$...$$` as well as mdBook's escaped
`\\(...\\)` / `\\[...\\]` delimiters. Do not enable KaTeX alongside it.
Use Markdown for text formatting, rather than original-book LaTeX commands
such as `\key{...}`. MathJax and TikZJax load from external sites, so the
local preview needs an internet connection.

Graphviz converts fenced `dot process` blocks into SVG during the build.
TikZ diagrams are handled separately by TikZJax in the browser.

## License
The license of the book is Creative Commons BY-NC-SA 4.0.
