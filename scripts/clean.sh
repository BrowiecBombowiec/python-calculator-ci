#!/bin/bash
set -e

rm -rf .pytest_cache
find . -type d -name "__pycache__" -exec rm -rf {} +