#!/bin/bash

last_index=$#
odwrotne=()
echo "Podana Array argumentow: $*"

for (( i=$last_index; i>0; i-- )); do
  odwrotne+=(${!i})
done
echo "Array argumentow w odwrotnej kolejnosci: ${odwrotne[@]}"

exit 0