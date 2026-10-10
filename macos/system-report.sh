#!/usr/bin/env bash
# Coleta somente leitura, sem alterar configurações.
set -euo pipefail
printf 'Sistema: '; uname -s
printf 'Arquitetura: '; uname -m
if command -v sw_vers >/dev/null 2>&1; then sw_vers; fi
printf '\nEspaço disponível:\n'
df -h /
