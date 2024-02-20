#!/bin/bash

if [ $# -ne 3 ]; then
  echo "Niewlasciwa ilosc argumentwo"
  exit 0
fi

# uruchom dodatnie.sh
bash dodatnie.sh $1 $2 $3 &
child=$!

# czeka az skrypt skonczy dzialanie
wait $child

#get result from child
res=$?
echo $res

if [ $res -eq 0 ]; then
  echo "bok ujemny lub 0"
  exit 0
fi

# sprawdz czy mozna zrobic trojkat z bokow a, b, c
a=$1
b=$2
c=$3
if [ $(($b+$c)) -lt $a ]; then
  echo "dwa dodane boki nie moga byc mnienjsze niz ten trzeci"
  echo "za duzy a"
  exit 0
fi
if [ $(($a+$c)) -lt $b ]; then
  echo "dwa dodane boki nie moga byc mnienjsze niz ten trzeci"
  echo "za duzy b"
  exit 0
fi
if [ $(($a+$b)) -lt $c ]; then
  echo "dwa dodane boki nie moga byc mnienjsze niz ten trzeci"
  echo "za duzy c"
  exit 0
fi

# wynik
echo "all triangulated"
exit 1