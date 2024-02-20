#!/bin/bash

resA=0
resB=0

# Trap for SIGUSR1 to start CraneA.sh and CraneB.sh
trap '
  echo "DOZORCA:"
  echo "Received SIGALRM. Starting Crane1.sh and Crane2.sh."
  ./CraneA.sh &
  PIDA=$!
  ./CraneB.sh &
  PIDB=$!
  # nie dziala kill -SIGUSR1 $PIDA
  sleep 1
  kill -SIGUSR1 $PIDA
' SIGALRM

trap '
  echo "DOZORCA:"
  echo "Received SIGUSR1. CraneA.sh has moved a file."
  if kill -0 "$PIDA" 2>/dev/null; then
    echo "D: craneA is runing there are files"
    resA=$(($resA+1))
    kill -SIGUSR1 $PIDB
  else
    echo "D: craneA not running Last time for B"
    kill -SIGUSR1 $PIDB
  fi
' SIGUSR1

trap '
  echo "DOZORCA:"
  echo "Received SIGUSR2. CraneB.sh has moved a file."
  resB=$(($resB+1))
  if kill -0 "$PIDB" 2>/dev/null; then
    echo "D: craneB is still running so there are files to move for craneA."
    kill -SIGUSR1 $PIDA
  else
    echo "D: craneB is not running, so A is not running too"
    kill -SIGQUIT $$
  fi
' SIGUSR2

trap '
  echo "DOZORCA:"
  echo "Received SIGINT. Stopping CraneA.sh and CraneB.sh."
  kill $PIDA
  resA=$?
  kill $PIDB
  resB=$?
  echo "CraneA.sh przeniosl $resA plikow"
  echo "D: CraneB.sh przeniosl $resB plikow"
  exit 0
' SIGINT  

trap '
  echo "DOZORCA:"
  echo "Koniec dzialania dozorcy"
  echo "CraneA.sh przeniosl $resA plikow"
  echo "CraneB.sh przeniosl $(($resB-1)) plikow"
  kill -TERM $$
' SIGQUIT


while true; do
  sleep 1
done

exit 0