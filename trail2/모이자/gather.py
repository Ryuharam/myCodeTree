import sys

n = int(input())
A = list(map(int, input().split()))

min_val = sys.maxsize

for i in range(n):
    sum = 0
    for j in range(n):
        sum += abs(i - j) * A[j]
    min_val = min(min_val, sum)

print(min_val)