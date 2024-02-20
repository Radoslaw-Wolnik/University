#!/bin/bash

if [[ ${#1} -gt ${#2} ]]
then
echo "napis '$1' jest dluzszy niz napis '$2'" 
elif [[ ${#1} -eq ${#2} ]]
then
echo "napisy sa rownej dlugosci"
else
echo "napis '$2' jest dluzszy niz napis '$1'" 
fi

if [[ "$1" < "$2" ]]
then
echo "$1 napis jest wczesniej w alfabecie niz $2"
elif [[ "$1" > "$2" ]]
then
echo "$2 napis jest wczesniej w alfabecie niz $1"
else
echo "napisy sa takie same"
fi

exit 0