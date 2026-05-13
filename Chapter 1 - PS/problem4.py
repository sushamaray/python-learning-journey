import os

#specify the directory you want to list
directory_path = '/study'

# Get all files and folders in the current directory
contents = os.listdir(directory_path)

# Print each item on a new line
for item in contents:
    print(item)