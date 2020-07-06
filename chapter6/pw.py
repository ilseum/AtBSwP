#! /usr/bin/env python3
# passwords

PASSWORDS = {'email': "F7minlBDDuvMJuxESSKHFhTxFtjVB6",
             'blog': "VmALvQyKAxiVH5G8v01if1MLZF3sdt",
             'luggage': 12345}

import sys
import pyperclip

if len(sys.argv) < 2:
    print("Usage: python pw.py [account] - copy account password")
    sys.exit()

account = sys.argv[1]

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print(f"Password for {account} copied to clipboard.")
else:
    print(f"There is no account names {account}")
