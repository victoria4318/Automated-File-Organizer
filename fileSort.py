import os # for operating system
import shutil # for movement

dir_name = input("Enter Directory Name: ")
# path.expanduser defines the path for you once a directory is inputted
directory = os.path.join(os.path.expanduser('~'), dir_name)

extensions = {
    ".jpg": "Images",
    ".png": "Images",
    ".jpeg": "Images",
    ".HEIC": "Images",
    ".heic": "Images",
    ".gif": "Images",
    ".mpg4": "Videos",
    ".mov": "Videos",
    ".doc": "Documents",
    ".docx": "Documents",
    ".pdf": "Documents",
    ".txt": "Documents",
    ".mp3": "Music",
    ".wav": "Music",
    ".pptx": "Powerpoint",
    ".ppt": "Powerpoint",
    ".zip": "Zip Files"
}

for filename in os.listdir(directory):
    file_path = os.path.join(directory, filename)

    if os.path.isfile(file_path):
        # taking out extension and making it lowercased to make sure no files are missed
        extension = os.path.splitext(file_path)[1].lower()

        if extension in extensions:
            folder_name = extensions[extension]

            folder_path = os.path.join(directory, folder_name)
            os.makedirs(folder_path, exist_ok=True)

            destination_path = os.path.join(folder_path, filename)
            shutil.move(file_path, destination_path)

            print(f"Moved {filename} to {folder_name} folder.")
        else:
            print(f"Skipped {filename} it is not a file.")

print("File organization complete!")