#!/bin/bash
set -e

source .venv/bin/activate
pylint app cli.py tests