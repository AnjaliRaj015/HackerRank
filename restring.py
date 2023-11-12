#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

def repeatedString(s, n):
    # Count the number of 'a's in a single repetition of the string
    count_in_single_repetition = s.count('a')

    # Calculate the number of repetitions needed for the first n characters
    repetitions = n // len(s)

    # Calculate the remaining characters beyond the complete repetitions
    remaining_chars = n % len(s)

    # Count the number of 'a's in the remaining substring
    count_in_remaining = s[:remaining_chars].count('a')

    # Calculate the total count of 'a's
    total_count = count_in_single_repetition * repetitions + count_in_remaining

    return total_count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
