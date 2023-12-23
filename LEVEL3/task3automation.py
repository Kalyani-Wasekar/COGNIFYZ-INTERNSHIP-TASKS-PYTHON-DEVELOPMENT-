import os
import shutil

def organize_files(source_folder, destination_folder):
    # Create the destination folder if it doesn't exist
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Iterate through each file in the source folder
    for filename in os.listdir(source_folder):
        source_path = os.path.join(source_folder, filename)

        # Check if it's a file
        if os.path.isfile(source_path):
            # Get the file extension
            _, file_extension = os.path.splitext(filename)

            # Create a folder for the extension if it doesn't exist
            extension_folder = os.path.join(destination_folder, file_extension[1:])
            if not os.path.exists(extension_folder):
                os.makedirs(extension_folder)

            # Move the file to the corresponding folder
            destination_path = os.path.join(extension_folder, filename)
            shutil.move(source_path, destination_path)
            print(f"Moved {filename} to {extension_folder}")

if __name__ == "__main__":
    # Specify the source and destination folders
    source_folder = "path/to/source/folder"
    destination_folder = "path/to/destination/folder"

    # Call the function to organize files
    organize_files(source_folder, destination_folder)
