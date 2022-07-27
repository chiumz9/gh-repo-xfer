import os
os.system("ls > filelist.txt")
with open('./filelist.txt') as f:
    files = f.read().splitlines()
filelist = "filelist.txt"

for file in files:
    if "py" not in file and "txt" not in file:
        command = f"trash ./{file}/.git"
        os.system(f"trash {command}")
        command = f"trash ./{file}/.github"
        os.system(f"trash {command}")
        command = f"trash ./{file}/.gitignore"
        os.system(f"trash {command}")

f.close()
