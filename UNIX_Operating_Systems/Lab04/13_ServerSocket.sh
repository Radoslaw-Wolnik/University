#!/bin/bash
fifo_path="myfifo"
if [ ! -p "$fifo_path" ]; then
    mkfifo "$fifo_path"
fi

# Server functionality in an infinite loop
while true; do
    read -r word < "$fifo_path"
    if [ -z "$word" ]; then
        echo "Client closed. Exiting server."
        break
    fi

    vowel_count=$(echo "$word" | grep -o -i '[aeiou]' | wc -l)
    echo "Word '$word' has $vowel_count vowels." > "$fifo_path"
done

rm -f "$fifo_path"
exit 0