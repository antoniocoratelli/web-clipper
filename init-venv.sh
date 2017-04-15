#!/bin/bash

DIR="$(dirname "${BASH_SOURCE[0]}")"
cd "$DIR" && \
mkdir venv && \
virtualenv --python=python3 venv && \
source venv/bin/activate && \
pip3 install -r requirements.txt && \
deactivate
