#! python3
'''
BulletPointAdder.py - Adds Wikipadia bullet points to the start
of each line of text on the clipboard
'''

import pyperclip
TEXT = pyperclip.paste()

# Separate lines and add stars.
LINES = TEXT.split('\n')

LINES = ["* " + line for line in LINES]
TEXT = '\n'.join(LINES)

pyperclip.copy(TEXT)
