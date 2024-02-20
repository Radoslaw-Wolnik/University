#!/bin/bash
pkill napis
# pkill -f "napis.sh"
if [ $? -eq 0 ]; then
  ehco "Succes"
  exit 0
fi
echo "Fail"
exit 1