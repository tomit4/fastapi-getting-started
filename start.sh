#!/usr/bin/env bash

source ./env/bin/activate &&
    fastapi dev app/main.py
