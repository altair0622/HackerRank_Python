#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    #apples = a + apples
    #oranges = b + oranges
    count_o = 0
    count_a = 0
    for i in apples:
        i += a
        if i <= t and i >=s:
            count_a +=1
    for j in oranges:
        j += b
        if j <= t and j >=s:
            count_o +=1 
    print(count_a)
    print(count_o)
if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
