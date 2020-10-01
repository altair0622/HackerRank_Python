#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cutTheSticks function below.
def cutTheSticks(arr):
    result = []
    result.append(len(arr))
    while len(arr)>0:
        new = []
        for i in arr:
            if i-min(arr)>0:
                new.append(i-min(arr))
        arr = new
        if len(arr)>0:
            result.append(len(arr))
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
