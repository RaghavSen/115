import os

source_file = 'main.txt'
destination_file = 'newfile.txt'
os.rename(source_file, destination_file)

print(f"File moved from {source_file} to {destination_file}")
