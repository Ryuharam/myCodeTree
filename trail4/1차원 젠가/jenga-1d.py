import sys

input = sys.stdin.readline

N = int(input())

nums = [int(input()) for _ in range(N)]

move1 = list(map(int, input().split()))
move2 = list(map(int, input().split()))

tmp = []
for i in range(N):
    if move1[0] <= i + 1 and i + 1 <= move1[1]:
        continue
    tmp.append(nums[i])

tmp2 = []
n = len(tmp)
for i in range(n):
    if move2[0] <= i + 1 and i + 1 <= move2[1]:
        continue
    tmp2.append(tmp[i])

print(len(tmp2))
for t in tmp2:
    print(t)