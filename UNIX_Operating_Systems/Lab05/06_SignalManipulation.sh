#!/bin/bash
sigint=true

trap '
  if $sigint; then
  echo "Jestem niesmiertelny!"
  fi
' SIGINT

trap '
    echo "nie reguj"
    sigint=false
' SIGHUP

while true; do
    sleep 1
done
exit 0