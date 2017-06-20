#! python3
'''
regex_search.py - opens all .txt files in a folder and searches for any line
                  that matches a user-supplied regular expression. The results
                  should be printed to the screen.
'''

import os
import re

target_folder = input("Enter the target foulder:\n")
os.chdir(target_folder)
target_files = os.listdir(target_folder)
target_files = [target for target in target_files if target.endswith('.txt')]
regex = re.compile(input('Enter the regular expression:\n'))
for file_name in target_files:
    file = open(file_name)
    for line in file.readlines():
        words = regex.findall(line)
        if words:
            print(file_name + ": " + str(words))
