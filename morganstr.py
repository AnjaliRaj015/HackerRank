#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'morganAndString' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#

def morganAndString(a, b):
    # Write your code here    
    ans = ''
    a += 'z'
    b += 'z'
    while len(a) > 0 or len(b) > 0:
        if len(a) > 0 and len(b) > 0:
            if a <= b:
                ans += a[0]            
                a = a[1:]       
            elif a > b:
                ans += b[0]
                b = b[1:]            
        elif len(a) == 0 and len(b) > 0:
            ans += b[0]
            b = b[1:]            
        elif len(b) == 0 and len(a) > 0:
            ans += a[0]
            a = a[1:]
    return ans.strip('z')

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        a = input()

        b = input()

        result = morganAndString(a, b)

        fptr.write(result + '\n')

    fptr.close()

