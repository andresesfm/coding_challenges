#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    A=arr
    swaps = 0
    for i in range(1, len(A)):
        curNum = A[i]
        k = 0
        for j in range(i-1, -2, -1):
            k = j
            if A[j] > curNum:
                A[j+1] = A[j]
            else:
                swaps = swaps +1
                break
        
        A[k+1] = curNum

    return swaps


if __name__ == '__main__':

    n = 4

    arr = [4, 3, 1, 2]

    res = minimumSwaps(arr)

    print(str(res) + '\n' + str(arr))#3

    n = 5

    arr = [2, 3, 4, 1, 5]

    res = minimumSwaps(arr)

    print(str(res) + '\n' + str(arr))#3

    n = 5

    arr = [1, 3, 5, 2, 4, 6, 7]

    res = minimumSwaps(arr)

    print(str(res) + '\n' + str(arr))#3
    
