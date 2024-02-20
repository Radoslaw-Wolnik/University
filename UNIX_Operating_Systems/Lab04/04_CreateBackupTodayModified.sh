#!/bin/bash
dzisiaj=$(date +%Y-%m-%d)
mkdir "$dzisiaj"

find ~ -maxdepth 1 -type f -newermt "$dzisiaj" ! -newermt "$dzisiaj+1 day" -exec cp {} "$dzisiaj" \;
echo "pliki utworzone dzisiaj skopiowane do: $dzisiaj"
exit 0