#!/bin/sh
set -ex

./clean.sh
test -d venv || python3 -m venv venv
./venv/bin/pip install build
./venv/bin/python -m build

ls -la ./dist
