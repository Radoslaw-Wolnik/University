#!/bin/bash

selw="CRANE A"
#also chyba $0
done="-SIGUSR1"
count=0
source="A"
dest="Buffor"
#move SIGUSR1
#stop SIGINT

function isEmpty(){
  if [ ! "$(ls -A $source)" ]; then
    echo "CRANE A:"
    echo "Source directory '$source' is empty.\n"
    return 255
  fi
  return 0
}


trap '
  echo "CRANE A:"
  echo "Started moving a file from '$source' to '$dest'."
  file=$(find $source -type f -maxdepth 1 | head -n 1)
  if [ -n "$file" ]; then
    mv "$file" $dest
    echo "A: Moved a file $file from '$source' to '$dest'."
    count=$(($count+1))
    kill $done $PPID
  else
    echo "CRANE A:"
    echo "Stopped moving files due to lack of them"
    if [ "$count" -lt 255 ]; then
      kill $done $PPID
      echo "A: $count"
      exit $count
    fi
    kill $done $PPID
    exit 0
  fi
' SIGUSR1

trap '
  echo "CRANE A: Stopped moving files. SIGINT"
  if [ "$count" -lt 255 ]; then
    exit $count
  fi
  exit 0
' SIGINT

while true; do
  sleep 1
done