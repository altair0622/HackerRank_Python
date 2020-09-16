#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulDays function below.
def beautifulDays(i, j, k):
    count = 0
    for num in range(i,j+1,1):
        n = num
        reversed_n = 0
        while n > 0:
            remainder = n % 10
            reversed_n = (reversed_n * 10) + remainder
            n = n // 10
        if abs(num-reversed_n)%k == 0:
            count +=1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ijk = input().split()

    i = int(ijk[0])

    j = int(ijk[1])

    k = int(ijk[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()
