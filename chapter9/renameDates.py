#! python3

import shutil
import os
import re

# Create regex
date_pattern = re.compile(r"^(.*?)"
                          r"(([01])?\d)"
                          r"(([0123])?\d)"
                          r"((19|20)\d{2})"
                          r"(.*?)$")

for american_name in os.listdir('.'):
    mo = date_pattern.search(american_name)

    if mo is None:
        continue

    before_part = mo.group(1)
    month_part = mo.group(2)
    day_part = mo.group(4)
    year_part = mo.group(6)
    after_part = mo.group(8)

    euro_filename = before_part + day_part + '-' + month_part + '-' + year_part + after_part

    abs_working_dir = os.path.abspath('.')
    american_name = os.path.join(abs_working_dir, american_name)
    euro_filename = os.path.join(abs_working_dir, euro_filename)
    print(f"Renaming {american_name} to {euro_filename}")
    # shutil.move(american_name, euro_filename)
