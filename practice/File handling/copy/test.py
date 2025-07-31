from __future__ import absolute_import
import os
from posixpath import abspath, dirname
import shutil

def printdir(dir):
    filenames = os.listdir(dir)
    print('List of Filename : '+str(filenames))
    for filename in filenames:
        print(filename)
        fullpath=os.path.join(dir,filename)
        print(fullpath)
        abspath=os.path.abspath(fullpath)
        print(abspath)
        dirname=os.path.dirname(abspath)
        print(dirname)
        file=os.path.basename(abspath)
        print(file)
        result=os.path.exists(dir)
        print(result)
        if filename != 'copy':
            if not os.path.isdir('copy'):
                os.mkdir('copy')

            shutil.copy(abspath, 'copy')
    
if __name__ == "__main__":
    dir = r'../file handling'
    printdir(dir)