import subprocess

# Define file data
file_data = [
    (0, "sample list", "/home/takuho/CODE/linux_tools/cmd_wrapper/cmd_list"),
    (1, "keyword01", "/home/takuho/CODE/linux_tools/cmd_wrapper/cmdw.sh"),
    (2, "keyword02", "/home/takuho/CODE/linux_tools/cmd_wrapper/cmdw.sh")
]

# Display list of keywords
print("File List:")
for index, keyword, path in file_data:
    print(f"{index} : {keyword}")

# Accept user input
selection = int(input("Enter the number of the file to display: "))

# Retrieve the path of the selected file
selected_file_path = None
for index, keyword, path in file_data:
    if index == selection:
        selected_file_path = path
        break

# Error message if file is not found
if selected_file_path is None:
    print("Invalid selection. The program will exit.")
else:
    # Display file content using 'less' command
    try:
        subprocess.run(["less", selected_file_path])
    except Exception as e:
        print(f"An error occurred: {e}")

