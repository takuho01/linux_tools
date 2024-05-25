#! /bin/bash

# Check for input arguments and set mode variable if --hoge format is found
mode=""
for arg in "$@"; do
	if [[ "$arg" =~ ^--(.+) ]]; then
		mode="${BASH_REMATCH[1]}"
	fi
done

if [[ "$mode" == "backup" ]]; then
	mode_selected_file=/home/takuho/CODE/linux_tools/single_scripts/backup_file.sh
	echo "mode_selected_file"
	echo "$mode_selected_file"
	echo "==============================="
	
	if [ -f "$mode_selected_file" ]; then
		# /bin/bash "$mode_selected_file" "$@"
		echo "this file needs some inputs"
	else
		echo "Error: Selected mode file does not exist."
	fi
elif [[ "$mode" == "hogo" ]]; then
  	echo "hogo"
elif [[ -z "$mode" ]]; then
  	echo "Error: No mode specified."
else
  	echo "no match"
	cat 
fi









