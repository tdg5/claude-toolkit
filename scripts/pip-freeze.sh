#!/usr/bin/env bash

set -eo pipefail

# From https://stackoverflow.com/a/4774063
REPO_DIR="$( cd -- "$(dirname "$0")/.." >/dev/null 2>&1 ; pwd -P )"
VENV_DIR="$REPO_DIR/venv"

if [ ! -d "$VENV_DIR" ]; then
  echo "Venv is not set up. Aborting."
  exit 1
fi

VERIFY=false
for arg in "$@"; do
  case "$arg" in
    --verify) VERIFY=true ;;
  esac
done

source "$VENV_DIR/bin/activate"

echo "Freezing requirements..."
pip freeze | grep -v '^\-e' > "$REPO_DIR/requirements.txt"

if [ "$VERIFY" = true ] && ! git diff --quiet requirements.txt; then
  echo "pip freeze caused file changes, verification failed."
  exit 1
fi
