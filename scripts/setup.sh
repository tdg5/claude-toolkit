#!/usr/bin/env bash

set -eo pipefail

# From https://stackoverflow.com/a/4774063
REPO_DIR="$( cd -- "$(dirname "$0")/.." >/dev/null 2>&1 ; pwd -P )"
VENV_DIR="$REPO_DIR/venv"

if [ ! -d "$VENV_DIR" ]; then
  echo "Creating virtual environment at $VENV_DIR..."
  python3 -m venv "$VENV_DIR"
fi

source "$VENV_DIR/bin/activate"

echo "Installing packages in development mode..."
pip install -r "$REPO_DIR/requirements.txt"
pip install -e "$REPO_DIR[dev]"
pip install -e "$REPO_DIR/packages/claude-toolkit-core"
pip install -e "$REPO_DIR/packages/claude-toolkit-cli"

echo "Freezing requirements..."
pip freeze | grep -v '^\-e' > "$REPO_DIR/requirements.txt"

echo "Setup complete."
