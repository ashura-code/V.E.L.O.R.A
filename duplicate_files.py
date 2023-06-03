import os
import hashlib

# Function to calculate the hash of a file
def calculate_file_hash(file_path):
    with open(file_path, 'rb') as file:
        data = file.read()
        file_hash = hashlib.md5(data).hexdigest()
    return file_hash

# Function to find and delete duplicate files
def delete_duplicate_files(directory_path):
    # Dictionary to store file hashes
    file_hashes = {}

    # Iterate over each file in the directory
    for root, dirs, files in os.walk(directory_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)

            # Calculate the hash of the file
            file_hash = calculate_file_hash(file_path)

            # Check if the file hash is already in the dictionary
            if file_hash in file_hashes:
                # Duplicate file found, delete it
                print(f"Duplicate file found: {file_path}")
                os.remove(file_path)
            else:
                # Add the file hash to the dictionary
                file_hashes[file_hash] = file_path

# Example usage
directory_to_scan = "C:/Users/sriva/Desktop/pic"
delete_duplicate_files(directory_to_scan)
