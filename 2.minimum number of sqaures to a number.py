A number can always be represented as a sum of squares of other numbers. Note that 1 is a square and we can always break a number as [(1 * 1) + (1 * 1) + (1 * 1) + …]. Given a number n, find the minimum number of squares that sum to n.
Sample Input 1:
100
Sample Output 1:
1
Explanation:
We can write 100 as 10^2 also, 100 can be written as (5^2) + (5^2) + (5^2) + (5^2), but this representation requires 4 squares. So, in this case, the expected answer would be 1, that is, 10^2.

#steps to follow for solving overlapping problems
#Step1: start implementing recursion solution
#Step2: then implement using DP
#Step3: finally try with iterative DP

#using recursion
import math, sys
from sys import setrecursionlimit
setrecursionlimit(10**6)

def minsq(n):

    if n == 0:
        return 0
    
    ans = sys.maxsize
    root = int(math.sqrt(n))
    for i in range(1, root + 1):
        currAns = 1 + minsq(n - (i ** 2))
        ans = min(ans, currAns)
    return ans

#using DP
def minsqd(n, dp):

    if n == 0:
        return 0

    ans = sys.maxsize
    root = int(math.sqrt(n))
    for i in range(1, root + 1):
        newCheck = n - (i ** 2)
        if dp[newCheck] == -1:
            smallAns = minsqdp(newCheck, dp)
            dp[newCheck] = smallAns
            currAns = 1 + smallAns
        else:
            currAns = 1 + dp[newCheck]

        ans = min(ans, currAns)
    return ans

#iterative
def iterative(n):
    dp = [-1 for in range(n+1)]
    dp[0] = 0
    for i in range(1, n+1):
        ans = sys.maxSize
        root = int(math.sqrt(i))
        for j in range(1, root + 1):
            currAns = 1 + dp[i-(j**2)]
            ans = min(ans, currAns)
        dp[i] = ans
    return dp[n]
    
n = int(input())
dp = [-1 for i in range(n + 1)]
print(minsq(n))
print(minsqdp(n, dp))
