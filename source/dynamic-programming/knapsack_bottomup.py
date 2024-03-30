def knapsack(i, j, weights, profits):
    dp = [[0] * (j+1) for _ in range(i+1)]

    for i in range(1, i+1):
        for j in range(1, j+1):
            if weights[i-1] <= j:
                dp[i][j] = max(dp[i-1][j], profits[i-1] + dp[i-1][j-weights[i-1]])
            else:
                dp[i][j] = dp[i-1][j]

    return dp[i][j]

n = 4
K = 5
W = [2, 1, 3, 2]
P = [12, 10, 20, 15]
print(knapsack(n, K, W, P))