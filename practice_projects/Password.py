#! python3
'''Password.py - An insecure password locker program'''

import sys
import pyperclip

PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
             'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
             'luggage': '12345'}

if len(sys.argv) < 2:
    print('Usage: python Password.py [account] - copy account password')
    sys.exit()

ACCOUNT = sys.argv[1]  # first command line arg is the account name

if ACCOUNT in PASSWORDS:
    pyperclip.copy(PASSWORDS[ACCOUNT])
    print('Password for ' + ACCOUNT + ' copied to clipboard.')
else:
    print('There is no account named ' + ACCOUNT)
