#!/usr/bin/env bash
set -e

if ! command -v buildozer >/dev/null 2>&1; then
  echo "buildozer not found. Installing to ~/.local/bin..."
  pip3 install --user buildozer
  export PATH=$PATH:~/.local/bin
fi

echo "Running buildozer android debug"
buildozer -v android debug
