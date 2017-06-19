#! python3
'''
mcb.pyw - Saves and loads pieces of text to the clipboard.
Usage: py mcb.pyw save <keyword> - Saves clipboard to keyword.
       py mcb.pyw delete <keyword> - Delete the content of keyword.
       py mcb.pyw <keyword> - Loads keyword to clipboard.
       py mcb.pyw list - Loads all keywords to clipboard.
'''

import shelve
import pyperclip
import sys

mcbShelf = shelve.open("mcb")
# Save clipboard content
if len(sys.argv) == 3:
    if sys.argv[1].lower() == 'save':
        mcbShelf[sys.argv[2]] = pyperclip.paste()
    elif sys.argv[1].lower() == 'delete':
        del mcbShelf[sys.argv[2]]
elif len(sys.argv) == 2:
    # List keywords and load content
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
mcbShelf.close()
