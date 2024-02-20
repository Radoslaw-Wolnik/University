#!/bin/bash

if [ $# -eq 0 ]; then
    username=$(whoami)
fi
username="$1"

home_directory=$(getent passwd "$username" | cut -d: -f6)

# Check if the user exists
if [ -z "$home_directory" ]; then
    echo "Error: User not found: $username"
    exit 1
fi

# Display information about the terminal file
echo "Information about terminal file for user: $username"
echo "Home Directory: $home_directory"
echo "Terminal File: $home_directory/.bashrc" 
exit 0