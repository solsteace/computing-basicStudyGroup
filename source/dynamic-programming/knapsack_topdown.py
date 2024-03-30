def knapsack(i, j, weights, profits, memo = None):
    if memo is None:
        memo = [[-1 for _ in range(j+1)] for _ in range(i+1)]

    if memo[i][j] != -1:
        return memo[i][j]
    
    if i == 0 or j == 0:
        return 0
    elif j - weights[i-1] >= 0:
        memo[i][j] = max(knapsack(i-1, j, weights, profits), profits[i-1] + knapsack(i-1, j-weights[i-1], weights, profits))
        return memo[i][j]
    else:
        memo[i][j] = knapsack(i-1, j, weights, profits)
        return memo[i][j]

n = 4
K = 5
W = [2, 1, 3, 2]
P = [12, 10, 20, 15]
print(knapsack(n, K, W, P))