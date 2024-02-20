#!/bin/bash

calculate_size() {
  local path="$1"
  local size=0

  if [ -f "$path" ]; then
    # If it's a regular file, get its size using stat
    size=$(stat -c "%s" "$path" 2>/dev/null || stat -f "%z" "$path" 2>/dev/null)
  elif [ -d "$path" ]; then
    # If it's a directory, calculate the total size of its contents recursively
    local sub_items=$(ls -A "$path")

    for item in $sub_items; do
      calculate_size "$path/$item"
      size=$((size + $?))  # $? result from last instruction
    done
  fi
  echo "$size"
}

ourpath="$1"
if [ ! -d "$ourpath" ]; then
    echo "Error: Nie ma folderu: $ourpath"
    exit 2
fi

result=$(calculate_size "$ourpath")

echo "Total size of $ourpath: $result bytes"
exit 0