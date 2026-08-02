import sys

input = sys.stdin.readline

N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

max_cnt = 0

for i in range(N-2):
    for j in range(N-2):
        sum_val = 0
        for r in range(3):
            for c in range(3):
                sum_val += arr[i+r][j+c]
        max_cnt = max(max_cnt, sum_val)

print(max_cnt)