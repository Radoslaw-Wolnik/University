#!/bin/bash
if [ $# -ne 3 ]; then
  echo "Niewlasciwa ilosc argumentwo"
  exit 0
fi
if [ $1 -le 0 ]; then
  echo "pierwszy arg mniejszy od zera lub rowny"
  exit 0
fi
if [ $2 -le 0 ]; then
  echo "drugi"
  exit 0
fi
if [ $3 -le 0 ]; then
  echo "trzeci"
  exit 0
fi

echo "all good"
exit 1