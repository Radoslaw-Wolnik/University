#!/bin/bash

if [ $# -eq 0 ]; then
  echo "Zaden argument nie zostal podany"
  echo "do better: $0 <filepath>"
  exit 1
fi 

path="$1"

if [ ! -e "$path" ]; then
  echo "Error: Plik nie istnieje: $path"
  exit 2
fi 

# Get the file extension
ext="${path##*.}"

case "$ext" in
  "txt")
    nano "$path" &
    ;;
  "sh")
    bash "$path"
    ;;
  *)   
    echo "Nieznany typ pliku: $ext"
    ;;
esac  

exit 0