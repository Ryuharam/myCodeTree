import sys

input = sys.stdin.readline

K, N = list(map(int, input().split()))
answer = []

def choose(idx: int):
    if idx == N:
        print(*answer)
        return

    for i in range(1, K+1):
        if idx > 1 and answer[-1] == answer[-2] and answer[-1] == i:
            continue

        answer.append(i)
        choose(idx + 1)
        answer.pop()

choose(0)