# Python File Organizer

*Organizes files from a user defined directory by their file type into user defined sub-folders. It supports a wide range of file types including images, videos, audio files, documents, powerpoint files, excel files, pdf files, and log files.*

## How it works

1. The script first asks for a source directory from the user. This is the directory that contains the files to be organized.

2. It then asks for a destination directory. This is where the organized files will be moved to. If the directory does not exist, it will be created.

3. The script then creates subdirectories in the destination directory for each file type.

4. It then walks through the source directory, renames all extensions to lowercase and moves each file to the corresponding subdirectory in the destination directory based on its file type.  If name already exists, moved file is renamed base_1_ext.

5. The script logs the movement of each file in a log file named `file_move_{current_date}.log`.

6. Finally, it prints a message to let the user know that the files have been moved and to check the log file.

### Usage

To run the script, simply execute it with a Python interpreter. It will prompt you for the source and destination directories.

### Dependencies

- os
- shutil
- datetime

*These are all within the standard Python library and will not need to be installed separately.*

#### Touch

*Text file with multiple lines of "touch" included to test script.*
