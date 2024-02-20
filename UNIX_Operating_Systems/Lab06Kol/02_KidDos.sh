#!/bin/bash

max=$1
min=$1
for (( i=$#; i>0; i-- )); do
  if [[ ${!i} -gt $max ]]; then
    max=${!i}
  elif [[ ${!i} -lt $min ]]; then
    min=${!i}
  fi
done


echo "scnd max: $max"
echo "scnd min: $min"

./thrd.sh $min $max &
wait
Tres=$?
echo "scnd got: $Tres"

exit $Tres