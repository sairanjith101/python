import os
import time

if os.path.isfile('kgf.txt'):
    print("File exists")
else:
    with open('kgf.txt', 'w') as file:
        print("file created successfully")

time.sleep(10)

os.rename('kgf.txt', 'kgf_part1.txt')
time.sleep(10)

os.remove('kgf_part1.txt')
time.sleep(10)

os.mkdir("KGF")
time.sleep(10)

os.path.exists("KGF")
time.sleep(10)