import os

os.chdir('/Users')
current = os.getcwd()
for folder, sub, files in os.walk(os.getcwd()):
    for file in files:
        whole = folder + '/' + file
        try:
            size = os.path.getsize(whole)
        except FileNotFoundError:
            continue

        if size > 500000000:
            print(f"{whole} ......... {size}")
