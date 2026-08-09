import sys

input = sys.stdin.readline

N, M = list(map(int, input().split()))

answer = []

# idx 자리에 num을 고르기/안고르기, 지금까지 cnt 개의 수 골랐고
def choose(idx: int, cnt: int, num: int):
    if cnt == M:
        print(*answer)
        return
    if idx >= M or num > N:
        return
    
    answer.append(num)
    choose(idx+1, cnt+1, num+1)
    answer.pop()

    choose(idx, cnt, num+1)

choose(0, 0, 1)
