#! python3
'''
regex_search.py - opens all .txt files in a folder and searches for any line
                  that matches a user-supplied regular expression. The results
                  should be printed to the screen.
'''

import os

target_folder = input("Enter the target foulder:\n")
os.chdir(target_folder)
target_files = os.listdir(target_folder)
target_files = [target for target in target_files if target.endswith('.txt')]
print(target_files)
