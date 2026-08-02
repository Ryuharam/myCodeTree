import sys

input = sys.stdin.readline

N, M = list(map(int, input().split()))

arr = [list(map(int, input().split())) for _ in range(N)]

total = 0

if N == 1 and M == 1:
    print(2)
    sys.exit()

# 행 순회
for r in range(N):
    same = 1
    max_val = 0
    flag = False
    for c in range(1,N):
        if arr[r][c] == arr[r][c-1]:
            if flag:
                same += 1
            else:
                flag = True
                same = 2
        else:
            flag = False
            same = 1
        max_val = max(max_val, same)
    if max_val >= M:
        total += 1

# 열 순회
for c in range(N):
    same = 1
    max_val = 0
    flag = False
    for r in range(1, N):
        if arr[r][c] == arr[r-1][c]:
            if flag:
                same += 1
            else:
                same = 2
                flag = True
        else:
            flag = False
            same = 1
        max_val = max(max_val, same)
    if max_val >= M:
        total += 1

print(total)
