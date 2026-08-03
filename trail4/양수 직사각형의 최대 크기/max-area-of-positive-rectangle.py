import sys

input = sys.stdin.readline

N, M = list(map(int, input().split()))

board = [list(map(int, input().split())) for _ in range(N)]

def is_all_plus(rs, re, cs, ce):
    for i in range(rs, re):
        for j in range(cs, ce):
            if board[i][j] <= 0:
                return False
    return True

max_size = -1

for rs in range(N + 1):
    for re in range(rs + 1, N + 1):
        for cs in range(M + 1):
            for ce in range(cs + 1, M + 1):
                if is_all_plus(rs, re, cs, ce):
                    max_size = max(max_size, (re - rs) * (ce - cs))

print(max_size)