#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the gridSearch function below.
def gridSearch(G, P):

    for g in range(len(G)):
        if P[0] in G[g]:
            condition = True
            ind_row = G.index(G[g])
            for j in range(len(G[g])-len(P[0])+1):
                if P[0] == G[g][j:j+len(P[0])]:
                    ind_col = j
                    for i in range(1,len(P)):
                        ind_row +=1
                        if P[i] == G[ind_row][ind_col:ind_col+len(P[0])]:
                            condition *= True
                        else:
                            condition = False
                            break
                    if condition:
                        return 'YES'
    return 'NO'





if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        RC = input().split()

        R = int(RC[0])

        C = int(RC[1])

        G = []

        for _ in range(R):
            G_item = input()
            G.append(G_item)

        rc = input().split()

        r = int(rc[0])

        c = int(rc[1])

        P = []

        for _ in range(r):
            P_item = input()
            P.append(P_item)

        result = gridSearch(G, P)

        fptr.write(result + '\n')

    fptr.close()
