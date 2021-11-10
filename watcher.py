import os
import sys
import time
import hashlib
# BUF_SIZE is totally arbitrary, change for your app!
BUF_SIZE = 65536  # lets read stuff in 64kb chunks!


def checkHash(fileName):
    md5 = hashlib.md5()
    with open(fileName, 'rb') as f:
        while True:
            data = f.read(BUF_SIZE)
            if not data:
                break
            md5.update(data)

    return md5.hexdigest()


start = checkHash(sys.argv[1])
sleep = 5
if len(sys.argv) > 3:
    sleep = int(sys.argv[3])

while True:
    current = checkHash(sys.argv[1])
    if current != start:
        start = current
        startTime = time.time()
        t = os.system(sys.argv[2] + " 2> nul")
        endTime = time.time()
        if t:
            continue
            print("Runtime ERROE")
        print("Took " +
              str(int(((endTime-startTime)*100))) + " millisecounds" +
              " with hash "+str(start)
              )
    time.sleep(sleep)
