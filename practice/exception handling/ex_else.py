#excepyion_else
try:
    fh = open('cheeta.txt', 'r')
    fh.write('HI I am RK')
except IOError:
    print("'cheeta.txt' does not exist")
else:
    print('file writen succesfully')