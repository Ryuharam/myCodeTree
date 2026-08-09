import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

answer = N

def move(idx: int, cnt: int):
    global answer

    if idx == N - 1:
        answer = min(answer, cnt)
        return
    
    if idx >= N:
        return
    
    for next in range(1, arr[idx] + 1):
        move(idx + next, cnt + 1)

move(0, 0)

if answer == N:
    print(-1)
else:
    print(answer)