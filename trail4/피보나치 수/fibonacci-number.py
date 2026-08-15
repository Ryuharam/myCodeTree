N = int(input())

memo = [-1 for _ in range(N+1)]

def memoization(n: int):
    if memo[n] != -1:
        return memo[n]

    if n <= 2:
        return 1

    memo[n] = memoization(n-2) + memoization(n-1)
    return memo[n]

print(memoization(N))
