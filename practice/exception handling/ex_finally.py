#exception_finally
try:
    fh = open('cheeta.txt', 'w')
    fh.read('Hi I am RK')
except TypeError:
    print("'cheeta file' does not exist")
finally:
    print('File written succesfully')