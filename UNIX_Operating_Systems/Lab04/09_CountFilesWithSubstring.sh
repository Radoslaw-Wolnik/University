#!/bin/bash
 
pod="$1"
echo "Podslowo: $pod"
count=$(find ~ -maxdepth 1 -type f -name "*$pod*" -o -type d -name "*$pod*" | wc -l)

echo "Ilosc plikow i folderow w pliku domowym zawierajace podlowo: '$pod'to: $count"

exit 0