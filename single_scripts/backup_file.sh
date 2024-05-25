#! /usr/bin/bash


# Get the current date and time in the format yyyymmddhhmm
current_datetime=$(date +%Y%m%d%H%M)

# Define the original file name and stop if no input is provided
if [ -z "$1" ]; then
    echo "Error: No input file provided."
    exit 1
fi
original_file=$1
# Create the backup file name using the original file name and the current date and time
backup_file_name="${original_file}_bkup${current_datetime}"

# Copy the original file to the new backup file
cp $original_file $backup_file_name

# Check if the backup file exists
if [ -f "$backup_file_name" ]; then
    echo "Backup was successful: $backup_file_name"
else
    echo "Error: Backup failed."
fi



