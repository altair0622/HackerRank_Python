#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the chocolateFeast function below.
def chocolateFeast(n, c, m):
    choco = n // c
    if choco >= m:
        wrapper = choco
        while wrapper > 0:
            wrapper = wrapper - m
            if wrapper >= 0:
                choco += 1
                wrapper += 1
    return choco
'''
choco = n//c
wrapper = choco
while wrapper>=m:
    a,b=divmod(wrapper, m)
    choco += a
    wapper = a + b
return choco
'''


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        ncm = input().split()

        n = int(ncm[0])

        c = int(ncm[1])

        m = int(ncm[2])

        result = chocolateFeast(n, c, m)

        fptr.write(str(result) + '\n')

    fptr.close()
