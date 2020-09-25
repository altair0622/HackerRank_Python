#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the viralAdvertising function below.
def viralAdvertising(n):
    cumul = 0
    init = 5
    while n > 0:
        
        liked = math.floor(init/2)
        cumul += liked
        init = liked*3
        n -=1
    return cumul

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()
