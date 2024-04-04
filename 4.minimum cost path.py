An integer matrix of size (M x N) has been given. Find out the minimum cost to reach from the cell (0, 0) to (M - 1, N - 1).
From a cell (i, j), you can move in three directions:
1. ((i + 1),  j) which is, "down"
2. (i, (j + 1)) which is, "to the right"
3. ((i+1), (j+1)) which is, "to the diagonal"
The cost of a path is defined as the sum of each cell's values through which the route passes.
 Input format :
The first line of the test case contains two integer values, 'M' and 'N', separated by a single space. They represent the 'rows' and 'columns' respectively, for the two-dimensional array/list.

The second line onwards, the next 'M' lines or rows represent the ith row values.

Each of the ith row constitutes 'N' column values separated by a single space.

Sample Input 1 :
3 4
3 4 1 2
2 1 8 9
4 7 8 1
Sample Output 1 :
13

#recursion solution
from sys import stdin
MAX_VALUE = 2147483647

def helper(mat, i, j, n, m):
    if i == n and j == m:
        return mat[i][j]
    if i > n or j > m:
        return MAX_VALUE

    ans1 = helper(mat, i + 1, j, n, m)
    ans2 = helper(mat, i, j + 1, n, m)
    ans3 = helper(mat, i + 1, j + 1, n, m)
    ans = mat[i][j] + min(ans1, ans2, ans3)
    return ans

def minCostPath(mat, mRows, nCols) :
    return helper(mat, 0, 0, mRows - 1, nCols - 1)


def take2DInput() :
    li = stdin.readline().rstrip().split(" ")
    mRows = int(li[0])
    nCols = int(li[1])
    
    if mRows == 0 :
        return list(), 0, 0
    
    mat = [list(map(int, input().strip().split(" "))) for row in range(mRows)]
    return mat, mRows, nCols


#main
mat, mRows, nCols = take2DInput()
print(minCostPath(mat, mRows, nCols))


#using recursive DP
def helper(mat, i, j, n, m, dp):
    if i == n and j == m:
        return mat[i][j]
    if i > n or j > m:
        return MAX_VALUE

    if dp[i+1][j] == MAX_VALUE:
        ans1 = helper(mat, i + 1, j, n, m, dp)
        dp[i+1][j] = ans1
    else:
        ans1 = dp[i+1][j]
    
    if dp[i][j+1] == MAX_VALUE:
        ans2 = helper(mat, i, j + 1, n, m, dp)
        dp[i][j+1] = ans2
    else:
        ans2 = dp[i][j+1]

    if dp[i+1][j+1] == MAX_VALUE:
        ans3 = helper(mat, i + 1, j + 1, n, m, dp)
        dp[i+1][j+1] = ans3
    else:
        ans3 = dp[i+1][j+1]
    
    ans = mat[i][j] + min(ans1, ans2, ans3)
    return ans

def minCostPath(mat, mRows, nCols, dp) :
    return helper(mat, 0, 0, mRows - 1, nCols - 1, dp)

#iterative DP solution - bottom up approach
def iterative(mat, mRows, nCols, dp):
    for i in range(mRows - 1, -1, -1):
        for j in range(nCols - 1, -1, -1):
            if i == mRows-1 and j == nCols-1:
                dp[i][j] = mat[i][j]
            else:
                ans1 = dp[i+1][j]
                ans2 = dp[i][j+1]
                ans3 = dp[i+1][j+1]
                dp[i][j] = mat[i][j] + min(ans1, ans2, ans3)
    return dp[0][0]

#top-down approach
def td(mat, n, m, dp):
    for i in range(1, n+1):
        for j in range(1, m+1):
            if i == 1 and j == 1:
                dp[i][j] = cost[0][0]
            else:
                ans1 = dp[i-1][j]
                ans2 = dp[i][j-1]
                ans3 = dp[i-1][j-1]
                dp[i][j] = mat[i-1][j-1] + min(ans1, ans2, ans3)
    return dp[n][m]


def take2DInput() :
    li = stdin.readline().rstrip().split(" ")
    mRows = int(li[0])
    nCols = int(li[1])
    
    if mRows == 0 :
        return list(), 0, 0
    
    mat = [list(map(int, input().strip().split(" "))) for row in range(mRows)]
    return mat, mRows, nCols


#main
mat, mRows, nCols = take2DInput()
dp = [[MAX_VALUE for j in range(nCols + 1)] for i in range(mRows + 1)]
print(minCostPath(mat, mRows, nCols, dp))
