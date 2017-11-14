#!python3
# deleting_unneeded_files.py - walks through a folder tree and searches for 
# exceptionally large files or folders. say, ones that have a file size of more
# than 100MB. Print these files with their absolute path to the screen.

import os
import shutil


def deleting_large_files(fd, mega):
    for foldername, subfolders, filenames in os.walk(fd):
        for filename in filenames:
            filepath = os.path.join(foldername, filename)
            size = os.path.getsize(filepath)
            size /= 1024 * 1024
            if size > mega:
                print(filepath)
                # os.unlink(filepath)


deleting_large_files("D:\\BaiduNetdiskDownload", 10)
