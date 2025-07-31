import os
import time

if os.path.isfile('new.txt'):
    print('file exists')
else:
    open('new.txt', 'w+')
time.sleep(5)

os.rename('new.txt','update.txt')
time.sleep(5)

os.mkdir('test')
time.sleep(5)