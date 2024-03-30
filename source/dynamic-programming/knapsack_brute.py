def knapsack(i, j, weights, profits):
    if i == 0 or j == 0:
        return 0
    elif j - weights[i-1] >= 0:
        return max(knapsack(i-1, j, weights, profits), profits[i-1] + knapsack(i-1, j-weights[i-1], weights, profits))
    else:
        return knapsack(i-1, j, weights, profits)

n = 4
K = 5
W = [2, 1, 3, 2]
P = [12, 10, 20, 15]
print(knapsack(n, K, W, P))