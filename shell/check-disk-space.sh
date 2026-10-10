#!/usr/bin/env bash
# Exemplo portátil para inspecionar um caminho local.
set -euo pipefail
df -h "${1:-.}"
