#_________________________________Class______________________________
import time
import sys

textSpeed = 0.04

def type(str):
  for c in str + '\n':
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(textSpeed)