#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the serviceLane function below.
def serviceLane(width, cases):

    line = width[int(cases[0]):int(cases[1])+1]
    low = 3
    for i in line:
        if i < low:
            low = i
    return low

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nt = input().split()

    n = int(nt[0])

    t = int(nt[1])

    width = list(map(int, input().rstrip().split()))

    #cases = []

    for _ in range(t):
        cases = list(map(int, input().rstrip().split()))

        result = serviceLane(width, cases)

        #fptr.write('\n'.join(map(str, result)))
        fptr.write(str(result))
        fptr.write('\n')

    fptr.close()
