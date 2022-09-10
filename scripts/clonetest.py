import os
lines = []
with open('./repolst.txt', 'r') as f:
    lines = f.readlines()
f.close()

for line in lines:
    os.system(f"git clone {line}")

