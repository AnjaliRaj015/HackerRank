# Here is my HackerRank Solutions

>The repository contains the solutions to various HackerRank problems.Organize the solutions so they are easy to navigate and understand. Each solution includes a reference to the problem statement and is well-documented to explain the logic and approach.


## Solution Approach

>In the "Solution Approach" section, provide a detailed explanation of your approach to solving the problem. Describe the algorithm, data structures, and any key insights that led to your solution. This helps others understand your thought process and learn from your solutions.

## 1. Taum and B'day

  - [Problem](https://www.hackerrank.com/challenges/taum-and-bday/problem?isFullScreen=true)(navigate to the Problem)
  - [Solution](.py) (navigate to the Solution file)
  - Problem Description
  >Taum is planning to celebrate the birthday of his friend, Diksha. There are two types of gifts that Diksha wants from Taum: one is black and the other is white. To make her happy, Taum has to buy black gifts and white gifts.

  - The cost of each black gift is `bc` units.
  - The cost of every white gift is `wc` units.
  - The cost to convert a black gift into a white gift or vice versa is `z` units.

Determine the minimum cost of Diksha's gifts.

 code with an example. Consider the following input:

```python
def taumBday(b, w, bc, wc, z):
    # Calculate the cost of buying all black gifts
    cost_black = min(bc, wc + z)
    
    # Calculate the cost of buying all white gifts
    cost_white = min(wc, bc + z)
    
    return b * cost_black + w * cost_white

```
- Explanation:
> Test Case #01:
Since black gifts cost the same as white, there is no benefit to converting the gifts. Taum will have to buy each gift for 1 unit. The cost of buying all gifts will be: 10 × 1 + 10 × 1 = 20.

> Test Case #02:
Again, he cannot decrease the cost of black or white gifts by converting colors.
z is too high. He will buy gifts at their original prices, so the cost of buying all gifts will be: 5 × 2 + 9 × 3 = 37.

#### Sample input & output

input
```
STDIN   Function
-----   --------
5       t = 5
10 10   b = 10, w = 10
1 1 1   bc = 1, wc = 1, z = 1
5 9     b = 5, w = 5
2 3 4   bc = 2, wc = 3, z = 4
3 6     b = 3, w = 6
9 1 1   bc = 9, wc = 1, z = 1
7 7     b = 7, w = 7
4 2 1   bc = 4, wc = 2, z = 1
3 3     b = 3, w = 3
1 9 2   bc = 1, wc = 9, z = 2
```

output
```
20
37
12
35
12
```
****

## 2. Find Digits

  - [Problem](https://www.hackerrank.com/challenges/find-digits/problem?isFullScreen=true)(navigate to the Problem)
  - [Solution](.py) (navigate to the Solution file)
  - Problem Description
  >Given an integer `n`, for each digit that makes up the integer, determine whether it is a divisor. Count the number of divisors occurring within the integer.

#### Compare The Triplets function will take parameters a and b which are the array of values of Alice and Bob.

 code with an example. Consider the following input:

```python
def findDigits(n):
    count = 0  # Initialize the count of divisors to 0
    num = n  # Create a copy of n for processing
    
    while num > 0:
        digit = num % 10  # Get the last digit of the number
        if digit != 0 and n % digit == 0:
            count += 1  # Increment count if digit is a divisor of n
        num //= 10  # Remove the last digit from the number
    
    return count
        

```

- Explanation:

> Test Case #1:
The number 12 is broken into two digits, 1 and 2. When 12 is divided by either of those two digits, the remainder is 0, so they are both divisors.

> Test Case #2:
The number 1012 is broken into four digits, 1, 0, 1, and 2. 1012 is evenly divisible by its digits 1, 1, and 2, but it is not divisible by 0 as division by zero is undefined.


#### Sample input & output
input
```
2
12
1012
```
output
```
2
3
```
****


## 3. Angry Professor

  - [Problem](https://www.hackerrank.com/challenges/angry-professor/problem?isFullScreen=true)(navigate to the Problem)
  - [Solution](.py) (navigate to the Solution file)
  - Problem Description
  >A Discrete Mathematics professor has a class of students. Frustrated with their lack of discipline, the professor decides to cancel class if fewer than some number of students are present when class starts. Arrival times go from on time (non-positive) to arrived late (positive). Given the arrival time of each student and a threshold number of attendees, determine if the class is canceled.

 code with an example. Consider the following input:

```python
def angryProfessor(k, a):
    on_time_students = sum(1 for arrival_time in a if arrival_time <= 0)
    if on_time_students < k:
        return "YES"
    else:
        return "NO"
        

```
- Explanation:
> Test Case #1:
The professor wants at least 3 students in attendance, but only 2 have arrived on time, so the class is canceled.

> Test Case #2:
The professor wants at least 2 students in attendance, and there are 3 who arrived on time, so the class is not canceled.

#### Sample input & output
input
```
2
4 3
-1 -3 4 2
4 2
0 -1 2 1
```
output
```
YES
NO
```
****

## 4. Solve Me First

  - [Problem](https://www.hackerrank.com/challenges/solve-me-first/problem?isFullScreen=true)(navigate to the Problem)
  - [Solution](.py) (navigate to the Solution file)
  - Problem Description
  >Complete the function `solveMeFirst` to compute the sum of two integers.

 code with an example. Consider the following input:

```python
def solveMeFirst(a,b):
    c = a + b
    return c

```

-Explanation
>The sum of 2 and 3 is 5.

#### Sample input & output
input
```
a = 2
b = 3
```
output
```
5
```
****

## 5. Beautiful Days at the Movies

  - [Problem](https://www.hackerrank.com/challenges/beautiful-days-at-the-movies?isFullScreen=true)(navigate to the Problem)
  - [Solution](.py) (navigate to the Solution file)
  - Problem Description:
  >beautifulDays(i, j, k) -> int`. Count the number of beautiful days in the range.


 code with an example. Consider the following input:

```python
def beautifulDays(i, j, k):
    beautiful_count = 0
    for day in range(i, j + 1):
        reverse_day = int(str(day)[::-1])
        if abs(day - reverse_day) % k == 0:
            beautiful_count += 1
    return beautiful_count
        

```
- Explanation
  >Lily may go to the movies on days 20, 21, 22, and 23. We perform the following calculations to determine which days are beautiful:
 - Day 20 is beautiful because ∣20−2∣=18 is evenly divisible by 6.
 - Day 21 is not beautiful because ∣21−12∣=9 is not evenly divisible by 6.
 - Day 22 is beautiful because ∣22−22∣=0 is evenly divisible by 6.
 - Day 23 is not beautiful because ∣23−32∣=9 is not evenly divisible by 6.
Only two days, 20 and 22, in this interval are beautiful. Thus, we return 2 as our answer.

#### Sample input & output
input
```
20 23 6

```
output
```
2
```
****


## 6. Sherlock and Squares

  - [Problem](https://www.hackerrank.com/challenges/sherlock-and-squares/problem?isFullScreen=true)(navigate to the Problem)
  - [Solution](.py) (navigate to the Solution file)
  - Problem Description:
  >    The squares function counts the number of square integers within a given range.


 code with an example. Consider the following input:

```python
def squares(a, b):
    # Find the square root of the lower and upper bounds
    sqrt_a = math.ceil(math.sqrt(a))
    sqrt_b = math.floor(math.sqrt(b))
    
    # Count the square integers in the range
    count = sqrt_b - sqrt_a + 1
    
    return count

```

- Explanation
  >Parameters:
    - a (int): the lower range boundary
    - b (int): the upper range boundary

  >Returns:
    - int: the number of square integers in the range

#### Sample input & output
input
```
2
3 9
17 24

```
output
```
2
0
```
****


## 7. Repeated String

  - [Problem](https://www.hackerrank.com/challenges/repeated-string/problem?isFullScreen=true)(navigate to the Problem)
  - [Solution](.py) (navigate to the Solution file)
  - Problem-Description:
  >    The repeatedString function calculates the frequency of the letter 'a' in the first n characters of a repeated infinite string.

 code with an example. Consider the following input:

```python
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

```

- Explanation
 >Parameters:
    - s (str): a string to repeat
    - n (int): the number of characters to consider

 >Returns:
    - int: the frequency of 'a' in the substring

#### Sample input & output
input
```
a
1000000000000
```
output
```
1000000000000
```
****


## 8. Cut the sticks

  - [Problem](https://www.hackerrank.com/challenges/cut-the-sticks/problem?isFullScreen=true)(navigate to the Problem)
  - [Solution](.py) (navigate to the Solution file)
  - Problem Description
  >    The cutTheSticks function calculates the number of sticks remaining before each iteration of cutting, discarding the shortest pieces until there are none left.

 code with an example. Consider the following input:

```python
def cutTheSticks(arr):
    result = []
    while len(arr) > 0:
        # Append the number of sticks before the cut
        result.append(len(arr))
        # Find the length of the shortest stick
        min_length = min(arr)
        # Cut all sticks by the length of the shortest stick
        arr = [x - min_length for x in arr if x - min_length > 0]
    return result

```
- Explanantion
  >Parameters:
    - arr (List[int]): a list of integers representing the lengths of each stick

>Returns:
    - List[int]: the number of sticks before each iteration

>Input Format:
    - The first line contains a single integer n, the size of arr.
    - The next line contains n space-separated integers, each an ai, where each value represents the length of the ith stick.

>Constraints:
    - 1 <= n <= 1000
    - 1 <= ai <= 1000

Example:

    Sample Input 0:
        6
        5 4 4 2 2 8

    Sample Output 0:
        [6, 4, 2, 1]

    Explanation 0:
        sticks-length        length-of-cut   sticks-cut
        5 4 4 2 2 8             2               6
        3 2 2 _ _ 6             2               4
        1 _ _ _ _ 4             1               2
        _ _ _ _ _ 3             3               1
        _ _ _ _ _ _           DONE            DONE

    Sample Input 1:
        8
        1 2 3 4 3 3 2 1

    Sample Output 1:
        [8, 6, 4, 1]

    Explanation 1:
        sticks-length         length-of-cut   sticks-cut
        1 2 3 4 3 3 2 1         1               8
        _ 1 2 3 2 2 1 _         1               6
        _ _ 1 2 1 1 _ _         1               4
        _ _ _ 1 _ _ _ _         1               1
        _ _ _ _ _ _ _ _       DONE            DONE

#### Sample input & output
input
```
8
1 2 3 4 3 3 2 1
```
output
```
8
6
4
1
```
****


## 9. Jumping on the Clouds

  - [Problem](https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem?isFullScreen=true)(navigate to the Problem)
  - [Solution](findthemedian.py) (navigate to the Solution file)
  - Problem-Description:
  >    The jumpingOnClouds function calculates the minimum number of jumps required to win the game by jumping on clouds. The player can jump on any cumulus cloud having a number that is equal to the number of the current cloud plus 1 or 2. The player must avoid the thunderheads.


 code with an example. Consider the following input:

```python
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
```

- Explanantion
>Parameters:
    - c (List[int]): an array of binary integers representing clouds (0 for safe clouds, 1 for thunderheads)

>Returns:
    - int: the minimum number of jumps required

>Input Format:
    - The first line contains an integer n, the total number of clouds.
    - The second line contains n space-separated binary integers describing clouds c where 0 indicates a safe cloud and 1 indicates a thunderhead.

>Constraints:
    - 2 <= n <= 100
    - c[i] belongs to {0, 1}

>Output Format:
    - Print the minimum number of jumps needed to win the game.

Example:

    Sample Input 0:
        7
        0 0 1 0 0 1 0

    Sample Output 0:
        4

    Explanation 0:
        The player must avoid clouds at indices 2 and 5. The game can be won with a minimum of 4 jumps.

    Sample Input 1:
        6
        0 0 0 0 1 0

    Sample Output 1:
        3

    Explanation 1:
        The only thundercloud to avoid is at index 4. The game can be won in 3 jumps.


#### Sample input & output
input
```
6
0 0 0 0 1 0
```
output
```
3
```
****

## 10. Morgan and a String

  - [Problem](https://www.hackerrank.com/challenges/morgan-and-a-string/problem?isFullScreen=true)(navigate to the Problem)
  - [Solution](.py) (navigate to the Solution file)
  - Problem-Description:
  >    The morganAndString function assembles the lexicographically minimal string made of two collections of uppercase letters. Morgan can take a letter from a collection only when it is on the top of the stack.


 code with an example. Consider the following input:

```python
def missingNumbers(arr, brr):
    count_a={}
    count_b={}
    for i in arr:
        count_a[i]=count_a.get(i,0)+1
    for i in brr:
        count_b[i]=count_b.get(i,0)+1
    missing=[]
    uni=set(arr+brr)
    for i in uni:
        count_d=count_b.get(i,0)-count_a.get(i,0)
        if count_d>0 and count_d<=100:
            missing.append(i)
    missing.sort()
    return missing

```
- Explanation

> Parameters:
    - a (string): Jack's letters
    - b (string): Daniel's letters

>Returns:
    - string: the completed string

>Input Format:
    - The first line contains an integer t, the number of test cases.
    - The next t pairs of lines are as follows:
        - The first line contains string a.
        - The second line contains string b.

>Constraints:
    - a and b contain only uppercase letters (ascii[A-Z]).
    - 1 <= |a|, |b| <= 10^5
    - 1 <= t <= 10

>Output Format:
    - For each test case, print the completed string.

Example:

    Sample Input:
    2
    JACK
    DANIEL
    ABACABA
    ABACABA

    Sample Output:
    DAJACKNIEL
    AABABACABACABA

Explanation:
    - For the first test case:
        - The first letters to choose from are J and D since they are at the top of the stack. D is chosen.
        - The options now are J and A. A is chosen.
        - The two stacks have J and N, so J is chosen.
        - The current string is DA.
        - Continue this way to the end to get the string DAJACKNIEL.

    - For the second test case:
        - Choose the lexicographically minimal letters at the top of the stacks to form the string AABABACABACABA.





#### Sample input & output
input
```
2
JACK
DANIEL
ABACABA
ABACABA
```
output
```
DAJACKNIEL
AABABACABACABA
```
****
