#!/bin/bash
read -p "Podaj liczbe calkowita a: " a
read -p "Podaj liczbe calkowita b: " b
read -p "Podaj liczbe calkowita c: " c
sum=$((a + b + c))
echo "Suma $a, $b, i $c to: $sum"
exit 0