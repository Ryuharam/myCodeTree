import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

arr.sort()

min_diff = max(arr)
for i in range(N):
    diff = arr[i+N] - arr[i]
    min_diff = min(min_diff, diff)

print(min_diff)