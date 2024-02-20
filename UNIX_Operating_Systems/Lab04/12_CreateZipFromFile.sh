#!/bin/bash

if [ $# -eq 0 ]; then
    echo "Usage: $0 <folder_path>"
    exit 1
fi
folder_path="$1"

if [ ! -d "$folder_path" ]; then
    echo "Error: Folder not found: $folder_path"
    exit 1
fi


current_user=$(whoami)
current_date=$(date +"%Y-%m-%d")

backup_folder="$HOME/backups"
mkdir -p "$backup_folder"


archive_filename="${current_user}_backup_data_${current_date}"
find "$folder_path" -type f -name "*.txt" -exec tar -cvzf "$backup_folder/$archive_filename.tar.gz" {} +

echo "Archive created: $backup_folder/$archive_filename.tar.gz"
exit 0
