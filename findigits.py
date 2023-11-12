#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'findDigits' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def findDigits(n):
    count = 0  # Initialize the count of divisors to 0
    num = n  # Create a copy of n for processing
    
    while num > 0:
        digit = num % 10  # Get the last digit of the number
        if digit != 0 and n % digit == 0:
            count += 1  # Increment count if digit is a divisor of n
        num //= 10  # Remove the last digit from the number
    
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = findDigits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
