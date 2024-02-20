#!/bin/bash

len=${#1}
rev=""
idx=$(($len-1))
echo "Podany string $1"

while [ $idx -ge 0 ]
do
  rev="${rev}${1:$idx:1}"
  idx=$(($idx-1))
done

echo "Odwrocony string: $rev"

exit 0