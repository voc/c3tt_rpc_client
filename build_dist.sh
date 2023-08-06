#!/bin/sh
set -ex

./clean.sh
test -d venv || python3 -m venv venv
./lint.sh
./venv/bin/pip install build
./venv/bin/python -m build

ls -la ./dist
