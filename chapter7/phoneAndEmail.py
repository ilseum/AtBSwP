#! python3

import pyperclip
import re

phone_regex = re.compile(r"((\d{3}|\(\d{3}\))?"
                         r"(\s|-|\.)?"
                         r"(\d{3})"
                         r"(\s|-|\.)"
                         r"(\d{4})"
                         r"(\s*(ext|x|ext.)\s*(\d{2,5}))?)")

email_regex = re.compile(r"("
                         r"[a-zA-Z0-9._%+-]+"
                         r"@"
                         r"[a-zA-Z0-9.-]+"
                         r"(\.[a-zA-Z]{2,4})"
                         r")")

# clipboard text
text = str(pyperclip.paste())
matches = []
for groups in phone_regex.findall(text):
    phone_number = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != "":
        phone_number += " x" + groups[8]
    matches.append(phone_number)
for groups in email_regex.findall(text):
    matches.append(groups[0])

# back to clipboard
if len(matches) > 0:
    pyperclip.copy("\n".join(matches))
    print("Copied to Clipboard:")
    print("\n".join(matches))
else:
    print("No phone numbers or email addresses found.")
