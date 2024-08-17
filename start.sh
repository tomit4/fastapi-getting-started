#!/usr/bin/env bash

if [ ! -d "./env" ]; then
    python3 -m venv env
fi

source ./env/bin/activate &&
    fastapi dev app/main.py
