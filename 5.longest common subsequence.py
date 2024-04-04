Given two strings, 'S' and 'T' with lengths 'M' and 'N', find the length of the 'Longest Common Subsequence'.
For a string 'str'(per se) of length K, the subsequences are the strings containing characters in the same relative order as they are present in 'str,' but not necessarily contiguous.
Subsequences contain all the strings of length varying from 0 to K.
Example :
Subsequences of string "abc" are:  ""(empty string), a, b, c, ab, bc, ac, abc.
Sample Input 1 :
adebc
dcadb
Sample Output 1 :
3
--> adb is common among both and longest, we can move it from left to right only. we can skip the character to form a subsequence

#recursive solution
def lcs(str1, str2, i, j):
    if i == len(str1) or j == len(str2):
        return 0
    
    if str1[i] == str2[j]:
        ans = 1 + lcs(str1, str2, i+1, j+1)
    else:
        ans1 = lcs(str1, str2, i+1, j)
        ans2 = lcs(str1, str2, i, j+1)
        ans = max(ans1, ans2)

    return ans

#recursive dp solution
def lcsdp(str1, str2, i, j, dp):
    if i == len(str1) or j == len(str2):
        return 0

    if str1[i] == str2[j]:
        if dp[i+1][j+1] == -1:
            smallans = lcsdp(str1, str2, i+1, j+1, dp)
            dp[i+1][j+1] = smallans
            ans = 1 + smallans
        else:
            ans = 1 + dp[i+1][j+1]
    else:
        if dp[i+1][j] == -1:
            ans1 = lcsdp(str1, str2, i+1, j, dp)
            dp[i+1][j] = ans1
        else:
            ans1 = dp[i+1][j]

        if dp[i][j+1] == -1:
            ans2 = lcsdp(str1, str2, i, j+1, dp)
            dp[i][j+1] = ans2
        else:
            ans2 = dp[i][j+1]
            
        ans = max(ans1, ans2)

    return ans

#iterative dp
def itr(str1, str2, i, j, dp):
    n = len(str1)
    m = len(str2)

    for i in range(n-1, -1, -1):
        for j in range(m-1, -1, -1):
            if str1[i] == str2[j]:
                dp[i][j] = 1 + dp[i+1][j+1]
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j+1])
    return dp[0][0]

str1 = input()
str2 = input()
n = len(str1)
m = len(str2)
dp = [[-1 for j in range(m+1)] for i in range(n+1)]
ans = lcsdp(str1, str2, 0, 0, dp)
