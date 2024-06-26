def fibonacci(n, memo = {}):
    if n in memo: return memo[n]
    if n == 0: return 0
    if n == 1: return 1
    memo[n] = fibonacci(n-1) + fibonacci(n-2)
    return memo[n]

print(fibonacci(1000))

# 2^50 = 
# dp : 50