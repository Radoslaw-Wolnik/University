#!/bin/bash
fifo_path="myfifo"
if [ ! -p "$fifo_path" ]; then
    echo "Error: Server not running. Start the server script first."
    exit 1
fi

read -p "Enter a word: " user_input
echo "$user_input" > "$fifo_path"
read -r length_calculation < "$fifo_path"

echo "$length_calculation"
echo "" > "$fifo_path"