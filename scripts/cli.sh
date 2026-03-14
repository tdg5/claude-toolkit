#!/usr/bin/env bash

set -eo pipefail

# From https://stackoverflow.com/a/4774063
REPO_DIR="$( cd -- "$(dirname "$0")/.." >/dev/null 2>&1 ; pwd -P )"

source "$REPO_DIR/venv/bin/activate"

exec python -m claude_toolkit_cli.main "$@"
