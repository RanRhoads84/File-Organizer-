# File mover
# Starts with user defined source dir
# then mkdir folders for each class
# then move files into the new folders
# Logs the movement of files
import os
import shutil
from datetime import datetime

# File types and Extensions are declared here
image_extensions = [".jpg", ".jpeg", ".jpe", ".jif", ".jfif", ".jfi", ".png", ".gif", ".webp", ".tiff", ".tif", ".psd", ".raw", ".arw", ".cr2", ".nrw",
                    ".k25", ".bmp", ".dib", ".heif", ".heic", ".ind", ".indd", ".indt", ".jp2", ".j2k", ".jpf", ".jpf", ".jpx", ".jpm", ".mj2", ".svg", ".svgz", ".ai", ".eps", ".ico"]

video_extensions = [".webm", ".mpg", ".mp2", ".mpeg", ".mpe", ".mpv", ".ogg",
                    ".mp4", ".mp4v", ".m4v", ".avi", ".wmv", ".mov", ".qt", ".flv", ".swf", ".avchd"]

audio_extensions = [".m4a", ".flac", ".mp3", ".wav", ".wma", ".aac"]
document_extensions = [".doc", ".docx", ".odt", ".txt", ".md"]
powerpoint_extensions = [".ppt", ".pptx"]
excel_extensions = [".xls", ".xlsx", ".xltx"]
pdf_extensions = [".pdf"]
logs = [".log"]

# Variable to call all file extensions
file_extensions = image_extensions + video_extensions + audio_extensions + \
    document_extensions + powerpoint_extensions + \
    excel_extensions + pdf_extensions + logs

# File types to be moved {Dictionary}
file_types = {
    "audio": audio_extensions,
    "documents": document_extensions,
    "excel": excel_extensions,
    "images": image_extensions,
    "installers": [".exe", ".msi"],
    "pdfs": pdf_extensions,
    "powerpoints": powerpoint_extensions,
    "videos": video_extensions,
    "z_logs": logs
}


# Function for Folder check, Will Create if required
def create_folders(dest_dir, folder_names):
    for folder_name in folder_names:
        folder_name = os.path.join(dest_dir, folder_name)
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
        else:
            pass


def dir_log(dest_dir, files):  # Function for Logging the movement of files
    # Get the current time with format [Year-Month-Day_Hour-Minute-Second]
    current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
    # Create a log file in the destination folder with current time
    log_file_name = os.path.join(dest_dir, f"file_move_{current_time}.log")
    with open(log_file_name, "w") as log:  # Open the log file in write mode
        for file in files:
            log.write(f"Moved {file} to {dest_dir} on {datetime.now()}\n")


# Function to Move files to the new folders function
def file_move(source_dir, dest_dir, file_types):
    moved_files = []
    for root, _, files in os.walk(source_dir):
        for file in files:
            file_extensions = os.path.splitext(file)[1].lower()
            for folder, extensions in file_types.items():
                if file_extensions in extensions:
                    filename = os.path.join(root, file)
                    destination_subdirectory = os.path.join(dest_dir, folder)
                    if not os.path.exists(destination_subdirectory):
                        os.makedirs(destination_subdirectory)
                    # While Loop to Rename file if already exists
                    counter = 1
                    destination_file = os.path.join(
                        destination_subdirectory, file)
                    while os.path.exists(destination_file):
                        base, extension = os.path.splitext(file)
                        new_file = f"{base}_{counter}{extension}"
                        destination_file = os.path.join(
                            destination_subdirectory, new_file)
                        counter += 1
                     # Function to move files
                    shutil.move(filename, destination_file)
                    moved_files.append(file)
    # Function to log the movement of files
    dir_log(dest_dir, moved_files)


# Get the source directory from the user
source_dir = input("Source Directory? \n")

# Reprint the source directory as Confirmation to the user
print(f"Confirmed Source Directory; \n {source_dir} \n")

# Confirm user Input
if not source_dir:
    print("Valid Source Directory Required, Exiting Program....")
    # Exit on no response
    exit()
else:  # Code execution continues
    print("Source Directory confirmed, Proceeding....")

# Choose output directory for moved files
dest_dir = input("Destination Directory? (Folder will be created) \n")
dest_dir = os.path.abspath(dest_dir)

#
# Reprint the destination directory as confirmation to the user
print(f" Destinion Folder confirmed as; \n {dest_dir} \n")

# Confirm user wishes to proceed
user_input = input("Press 'Y' to continue or 'N' to exit: ")

if user_input.lower() == 'n':
    print("Operation cancelled by user.")
    exit(0)  # Exit the script
elif user_input.lower() == 'y' or user_input == '' or user_input == ' ':
    print("Continuing operation...")
    # Continue with the rest of your code here
else:
    print("Invalid input. Please enter 'Y', 'N', Spacebar or Enter.")
# Create the folders for the file types
create_folders(dest_dir, file_types.keys())

# Move the files to the new folders
file_move(source_dir, dest_dir, file_types)

# Verify the files have been moved
print("Files have been moved, Check your log file")

# Exit the program
input("Press Enter to exit")
exit()
