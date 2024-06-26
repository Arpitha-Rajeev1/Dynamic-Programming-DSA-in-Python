Given a positive integer 'n', find and return the minimum number of steps that 'n' has to take to get reduced to 1. You can perform any one of the following 3 steps:
1.) Subtract 1 from it. (n = n - ­1) ,
2.) If n is divisible by 2, divide by 2.( if n % 2 == 0, then n = n / 2 ) ,
3.) If n is divisible by 3, divide by 3. (if n % 3 == 0, then n = n / 3 ).  
Input format :
The first and the only line of input contains an integer value, 'n'.
Output format :
Print the minimum number of steps.
Constraints :
1 <= n <= 10 ^ 6
Time Limit: 1 sec
Sample Input 1 :
4
Sample Output 1 :
2 
Explanation of Sample Output 1 :
For n = 4
Step 1 :  n = 4 / 2  = 2
Step 2 : n = 2 / 2  =  1 
Sample Input 2 :
7
Sample Output 2 :
3
Explanation of Sample Output 2 :
For n = 7
Step 1 :  n = 7 ­- 1 = 6
Step 2 : n = 6  / 3 = 2 
Step 3 : n = 2 / 2 = 1  


from sys import stdin
from sys import maxsize
import sys
from sys import setrecursionlimit
setrecursionlimit(10**6)

#recursive
def minSteps(n):
    if n == 1:
        return 0

    ans1 = sys.maxsize
    if n % 3 == 0:
        ans1 = minSteps(n // 3)
    if n % 2 == 0:
        ans2 = minSteps(n // 2)
    ans3 = minSteps(n-1)

    ans = 1 + min(ans1, ans2, ans3)

    return ans
    

#recursive dp
def minSteps(n, dp) :
    if n == 1:
        return 0
    
    ans1 = sys.maxsize
    if n % 3 == 0:
        if dp[n // 3] == -1:
            ans1 = minSteps(n // 3, dp)
            dp[n // 3] = ans1
        else:
            ans1 = dp[n // 3]
        
    ans2 = sys.maxsize
    if n % 2 == 0:
        if dp[n // 2] == -1:
            ans2 = minSteps(n // 2, dp)
            dp[n // 2] = ans2
        else:
            ans2 = dp[n // 2]
    
    if dp[n - 1] == -1:
            ans3 = minSteps(n - 1, dp)
            dp[n - 1] = ans3
    else:
        ans3 = dp[n - 1]

    ans = 1 + min(ans1, ans2, ans3)
    return ans

#main
n = int(stdin.readline().rstrip())
dp = [-1 for i in range(n + 1)]
print(minSteps(n, dp))
