"""
Module 2 — Activity: File Sorting with os and shutil
Student: [Bundalian, Clarence James L.]
Date: [09/27/2026]

============================================
WHAT DID YOU BUILD? (I built a Python script that organizes files automatically. It sorts files into folders based on their file extension)
============================================
[My script automatically organizes files into folders. It checks each file's extension]


============================================
KEY VOCABULARY
============================================
- os module: Works with files and folders
- shutil module: Moves or copies files.
- file path: The location of a file on the computer.
- directory: A folder that stores files.
(add more as needed)


============================================
YOUR SCRIPT
============================================
Paste the code you already wrote for this activity below.
"""

import os
import shutil

source_folder = "files"

for file in os.listdir(source_folder):
    file_path = os.path.join(source_folder, file)

    if os.path.isfile(file_path):
        ext = file.split(".")[-1].lower()
        folder = os.path.join(source_folder, ext)

        os.makedirs(folder, exist_ok=True)
        shutil.move(file_path, os.path.join(folder, file))


"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
[I used the wrong folder path at first, so the script could not find my files. But i fixed it
after that then my problem next is i cant list the file on the folders.]


============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional: how is this similar to what real automation scripts do?
think about your own gradebook/attendance workflow — could something
like this save you time there?]
"""
