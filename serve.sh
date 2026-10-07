#!/bin/sh
# Preview the book locally:  ./serve.sh
set -e
cd "$(dirname "$0")"
export PATH="$PWD/.tools/bin:$PATH"

if ! command -v mdbook >/dev/null; then
    echo "mdbook non trovato. Installa gli stessi strumenti della CI:"
    echo "  cargo install --locked --version 0.5.2 --root .tools mdbook"
    echo "  cargo install --locked --version 0.3.1 --root .tools mdbook-graphviz"
    exit 1
fi

# Build outside the repository on purpose. macOS stores extended attributes
# on non-APFS volumes (this drive is exFAT) in AppleDouble "._*" sidecars.
# A sidecar is deleted together with its parent file, so mdBook's
# stale-output cleanup lists it, deletes the parent, then fails to delete
# the sidecar that already went with it -- and every rebuild dies with
# "failed to remove book/._book-<hash>.js". That breaks live reload
# silently: the error lands in this log, never in the browser.
DEST="${TMPDIR:-/tmp}/cphb-rs-book"

echo "Serving on http://127.0.0.1:3000  (build dir: $DEST)"
exec mdbook serve --hostname 127.0.0.1 --port 3000 --dest-dir "$DEST" "$@"
