#!/bin/sh
set -ex

./clean.sh
./build_dist.sh
./venv/bin/pip install twine
./venv/bin/python -m twine upload dist/*
