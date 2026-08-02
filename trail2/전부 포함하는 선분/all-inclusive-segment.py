import sys

input = sys.stdin.readline

N = int(input())

coord = []

for _ in range(N):
    coord.append(list(map(int, input().split())))

start_sorted = sorted(coord, key = lambda x : x[0])
end_sorted = sorted(coord, key = lambda x : x[1])

# 가장 왼쪽 선분 제거
if start_sorted[0] == end_sorted[-1]:
    diff1 = end_sorted[-2][1] - start_sorted[1][0]
else:
    diff1 = end_sorted[-1][1] - start_sorted[1][0]

# 가장 오른쪽 선분 제거
if start_sorted[0] == end_sorted[-1]:
    diff2 = end_sorted[-2][1] - start_sorted[1][0]
else:
    diff2 = end_sorted[-2][1] - start_sorted[0][0]

print(min(diff1, diff2))