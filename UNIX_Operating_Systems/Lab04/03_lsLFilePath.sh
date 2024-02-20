#!/bin/bash

if [ $# -eq 0 ]; then
  echo "Wywolujac program napisz: $0 <file_path>"
  exit 1
fi

path="$1"

if [ -e "$path" ]; then
  echo "informacje ls -l"
  ls -l "$path"
else
  echo "zla scierzka nie ma pliku/folderu"
  exit 2
fi

exit 0