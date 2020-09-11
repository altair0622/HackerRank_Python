#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    high = scores[0]
    low = scores[0]
    count_low, count_high = 0,0
    for i in scores[1:]:
        if i > high:
            high = i
            count_high +=1
        elif i < low:
            low = i
            count_low +=1

    return count_high, count_low



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
