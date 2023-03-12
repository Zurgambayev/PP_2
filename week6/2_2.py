import os

path = "/Users/zeinaddinzurgambayev/pp2/week4" # Replace with the actual path to the directory you want to list files and directories in

# List directories
print("Directories:")
with os.scandir(path) as directory:
    for entry in directory:
        if entry.is_dir():
            print(entry.name)

# List files
print("\nFiles:")
with os.scandir(path) as directory:
    for entry in directory:
        if entry.is_file():
            print(entry.name)

# List all directories and files
print("\nAll directories and files:")
for root, directories, files in os.walk(path):
    for directory in directories:
        print(os.path.join(root, directory))
    for file in files:
        print(os.path.join(root, file))