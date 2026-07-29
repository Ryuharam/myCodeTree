import sys

input = sys.stdin.readline

n, m = tuple(map(int, input().split()))
live = input().split()

cnt = 0

for i in range(n):
    if live[i] == '0':
        continue
    cnt += 1
    for j in range(2 * m + 1):
        if i + j < n:
            live[i+j] = '0'

print(cnt)