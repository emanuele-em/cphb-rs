# cphb-rs
Competitive Programming Handbook - Rust Edition

## Local preview

Install [Graphviz](https://graphviz.org/download/) (`brew install graphviz`
on macOS or `sudo apt-get install graphviz` on Ubuntu), then install the
same build tools used by CI:

```sh
cargo install --locked --version 0.5.2 --root .tools mdbook
cargo install --locked --version 0.3.1 --root .tools mdbook-graphviz
export PATH="$PWD/.tools/bin:$PATH"
mdbook serve --hostname 127.0.0.1 --port 3000
```

Open <http://127.0.0.1:3000>. Use `mdbook build` for a static build in `book/`.

`./serve.sh` wraps the two steps above and builds into a temporary
directory rather than `book/`. That matters on a working copy that lives
on a non-APFS volume: macOS keeps extended attributes there in AppleDouble
`._*` sidecars, a sidecar is deleted together with its parent file, and
mdBook's stale-output cleanup then fails to remove a sidecar that has
already gone -- so every rebuild dies and live reload stops silently.

Run `mdbook test` to compile and run every Rust code block in the book.
CI runs it on every push, so a snippet that does not compile fails the build.
Blocks that cannot compile standalone are tagged `rust, ignore`; blocks that are
meant to be rejected by the compiler are tagged `rust, compile_fail`.

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
