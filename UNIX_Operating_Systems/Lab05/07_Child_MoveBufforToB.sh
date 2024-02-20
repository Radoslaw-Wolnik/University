#!/bin/bash

selw="CRANE B"
#also chyba $0
done="-SIGUSR2"
count=0
source="Buffor"
dest="B"
#move SIGUSR1
#stop SIGINT

function IsEmpty(){
  if [ ! "$(ls -A $source)" ]; then
    echo "CRANE B:"
    echo "Source directory '$source' is empty."
    return 255
  fi
  return 0
}

trap '
  echo "CRANE B:"
  echo "Started moving a file from '$source' to '$dest'."
  file=$(find $source -type f -maxdepth 1 | head -n 1)
  if [ -n "$file" ]; then
    mv "$file" $dest
    echo "CRANE B: Moved a file $file from '$source' to '$dest'."
    count=$(($count+1))
    kill $done $PPID
  else
    echo "CRANE B:"
    echo "Stopped moving files due to lack of them"
    if [ "$count" -lt 255 ]; then
      kill $done $PPID
      echo "B: $count"
      exit $count
    fi
    kill $done $PPID
    exit 0
  fi
' SIGUSR1

trap '
  echo "$selw: Stopped moving files. SIGINT"
  if [ "$count" -lt 255 ]; then
    exit $count
  fi
  exit 0
' SIGINT

while true; do
  sleep 1
done