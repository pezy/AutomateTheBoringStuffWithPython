#!python3
# selective_copy.py - walks through a folder tree and searches for files with a
# certain file extension (such as .pdf or .jpg). Copy these files from whatever
# location they are in to a new folder.

import os
import shutil


def selective_copy(flr, ext, new_flr):
    if not os.path.exists(new_flr):
        os.mkdir(new_flr)
    base = os.path.basename(new_flr)

    for foldername, subfolders, filenames in os.walk(flr):
        new_base = os.path.basename(foldername)
        if base == new_base:
            continue

        for filename in filenames:
            if filename.endswith(ext):
                filepath = os.path.join(foldername, filename)
                new_filepath = os.path.join(new_flr, filename)
                shutil.move(filepath, new_filepath)


selective_copy("C:\\Users\\pezy\\Downloads", ('.exe', '.msi'),
               "C:\\Users\\pezy\\Downloads\\Software")
