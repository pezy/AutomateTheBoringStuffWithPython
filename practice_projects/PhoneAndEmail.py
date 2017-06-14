#! python3
'''
PhoneAndEmail.py - Finds phone numbers and email addresses on the clipboard.
'''

import re
import pyperclip

PHONE_REGEX = re.compile(r'''(
    (\d{3}|\(\d{3}\))?              # area code
    (\s|-|\.)?                      # separator
    (\d{3})                         # first 3 digits
    (\s|-|\.)                       # separator
    (\d{4})                         # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  # extension
    )''', re.VERBOSE)

EMAIL_REGEX = re.compile(r'''(
    [a-zA-Z0-9._%+-]+   # username
    @                   # @ symbol
    [a-zA-Z0-9.-]+      # domain name
    (\.[a-zA-Z]{2,4})   # dot-something
    )''', re.VERBOSE)

TEXT = str(pyperclip.paste())
MATCHES = []
for groups in PHONE_REGEX.findall(TEXT):
    phone_num = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phone_num += ' x' + groups[8]
    MATCHES.append(phone_num)
for groups in EMAIL_REGEX.findall(TEXT):
    MATCHES.append(groups[0])

if len(MATCHES) > 0:
    pyperclip.copy('\n'.join(MATCHES))
    print('Copied to clipboard:')
    print('\n'.join(MATCHES))
else:
    print('No phone numbers or email addresses found.')
