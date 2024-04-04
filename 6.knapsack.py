A thief robbing a store can carry a maximal weight of W into his knapsack. There are N items, and i-th item weigh 'Wi' and the value being 'Vi.' What would be the maximum value V, that the thief can steal?

Sample Input 1 :
4
1 2 4 5
5 4 8 6
5
Sample Output 1 :
13


from sys import stdin

#recursive code
def knapsack(weights, values, n, maxWeight, i) :
    if i == n:
        return 0

    if weights[i] > maxWeight:
        ans = knapsack(weights, values, n, maxWeight, i+1)
    else:
        # including the ith item
        ans1 = values[i] + knapsack(weights, values, n, maxWeight - weights[i], i+1)
        # excluding the ith item
        ans2 = knapsack(weights, values, n, maxWeight, i+1)
        ans = max(ans1, ans2)

    return ans

#recursive dp - wrong solution
def knapsackdp(weights, values, n, maxWeight, i, dp):
    if i == n or maxWeight == 0:
        return 0

    if weights[i] > maxWeight:
        if dp[i+1][maxWeight] == 0:
            ans = knapsack(weights, values, n, maxWeight, i+1, dp)
            dp[i+1][maxWeight] = ans
        else:
            ans = dp[i+1][maxWeight]
    else:
        if dp[i+1][maxWeight - weights[i]] == 0:
            ans1 = val[i] + knapsack(weights, values, n, maxWeight - weights[i], i+1, dp)
            dp[i+1][maxWeight - weights[i]] = ans1
        else:
            ans1 = dp[i+1][maxWeight - weights[i]]

        if dp[i+1][maxWeight] == 0:
            ans2 = knapsack(weights, values, n, maxWeight, i+1, dp)
            dp[i+1][maxWeight] = ans2
        else:
            ans2 = dp[i+1][maxWeight]

        ans = max(ans1, ans2)

    return ans
    

def takeInput() :
    n = int(stdin.readline().rstrip())

    if n == 0 :
        return list(), list(), n, 0

    weights = list(map(int, stdin.readline().rstrip().split(" ")))
    values = list(map(int, stdin.readline().rstrip().split(" ")))
    maxWeight = int(stdin.readline().rstrip())

    return weights, values, n, maxWeight

#iterative DP
def knapsack(weights, values, n, maxWeight, i, dp):

    for i in range(1, n+1):
        for j in range(1, maxWeight+1):

            if j < weights[i-1]:
                ans = dp[i-1][j]
            else:
                ans1 = values[i-1] + dp[i-1][j-weights[i-1]]
                ans2 = dp[i-1][j]
                ans = max(ans1, ans2)
            dp[i][j] = ans

    return dp[n][maxWeight]

#main
weights, values, n, maxWeight = takeInput()
dp = [[0 for j in range(maxWeight+1)] for i in range(n+1)]
print(knapsack(weights, values, n, maxWeight, 0))
