#this is a comment

def w(path):
    with open(path, "w+") as output:
        text = open('./oldquine.py').read()
        output.write(text)

import os, sys, threading
MAX_OUTPUT = 750
try:
    os.mkdir('./output')
except:
    pass

nt = 1
for i in range(0, 1):
    for j in range(0, nt):
        threads = [None] * nt
        path = './output/oldquine' + str(i)
        threads[j] = threading.Thread(target=w, args=path)
        threads[j].start()



