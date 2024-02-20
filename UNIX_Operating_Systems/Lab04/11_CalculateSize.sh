#!/bin/bash

if [ $# -eq 0 ]; then
    echo "do: $0 <folder_path>"
    exit 1
fi

path="$1"

if [ ! -d "$path" ]; then
    echo "Error: Nie ma folderu: $path"
    exit 2
fi

du -h "$path"
exit 0
