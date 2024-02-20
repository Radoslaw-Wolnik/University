#!/bin/bash

if [ $# -eq 0 ]; then
  echo "Nei podano zadnych argumentow"
  exit 1
fi

av=$(echo "$*" | tr ' ' '\n' | awk '{total += $1 } END { print total / NR }' | bc)

echo "Srednia: $av"
exit 0