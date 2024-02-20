#!/bin/bash
declare -i sum
sum=$1+$2
result=$(($1+$2+$3))
echo "dodane dwie: $sum"
echo "dodane trzy: $result"
exit 0