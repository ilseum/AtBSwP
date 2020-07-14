#! python3

import zipfile
import os


def backup_to_zip(folder):
    folder = os.path.abspath(folder)

    number = 1
    while True:
        zip_filename = f"{os.path.basename(folder)}_{str(number)}.zip"
        if not os.path.exists(zip_filename):
            break
        number += 1

    # create zip file
    print(f"Creating {zip_filename}...")
    backup_zip = zipfile.ZipFile(zip_filename, 'w')

    for folder_name, subfolders, filenames in os.walk(folder):
        print(f"Adding files in {folder_name}")
        backup_zip.write(folder_name)
        for filename in filenames:
            new_base = os.path.basename(folder) + '_'
            if filename.startswith(new_base) and filename.endswith('.zip'):
                continue
            backup_zip.write(os.path.join(folder_name, filename))
    backup_zip.close()

    print("Done.")
