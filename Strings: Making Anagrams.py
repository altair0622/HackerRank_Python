#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the makeAnagram function below.
def makeAnagram(a, b):
    count = 0
    for i in a:
        if b.find(i) != -1:
            b = b[:b.find(i)] + b[b.find(i)+1:]
        else:
            count+=1
    return count+len(b)
            



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
