#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):
    start = 0
    nex = (start+k) % len(c)
    point = 0

    while nex != 0:
        if c[nex] == 1:
            point += 3
        else:
            point += 1
        nex = (nex+k) % len(c)
    if c[nex] == 1:
        point +=3
    else:
        point +=1

    return 100-point


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    fptr.write(str(result) + '\n')

    fptr.close()
