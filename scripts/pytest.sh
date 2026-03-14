#!/usr/bin/env bash

set -eo pipefail

# From https://stackoverflow.com/a/4774063
REPO_DIR="$( cd -- "$(dirname "$0")/.." >/dev/null 2>&1 ; pwd -P )"
VENV_DIR="$REPO_DIR/venv"

if [ ! -d "$VENV_DIR" ]; then
  echo "Venv is not set up. Aborting."
  exit 1
fi

source "$VENV_DIR/bin/activate"

EXIT_CODE=0
cd "$REPO_DIR"
for PACKAGE in $(find packages -maxdepth 1 -mindepth 1 -type d); do
  cd "$PACKAGE"
  coverage run -m pytest || EXIT_CODE=$?
  cd "$REPO_DIR"
done

coverage combine packages/*/.coverage
coverage report
coverage html -d "$REPO_DIR/.meta/coverage/html"

exit $EXIT_CODE
