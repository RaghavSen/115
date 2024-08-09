import os

# Define the source file path
source_file = 'main.txt'

# Define the destination file path
destination_file = 'newfile.txt'

# Rename (or move) the file
os.rename(source_file, destination_file)

print(f"File moved from {source_file} to {destination_file}")
