import os

# Specify the directory path (or use '.' for current directory)
directory_path = '/'  # You can change this to any valid path

# Get the list of contents
contents = os.listdir(directory_path)

# Print each item
print(f"Contents of directory '{directory_path}':")
for item in contents:
    print(item)