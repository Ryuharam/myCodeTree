import sys, math

input = sys.stdin.readline

N, M = list(map(int, input().split()))

coord = []
for _ in range(N):
    x, y = list(map(int, input().split()))
    coord.append((x, y))

def get_pow_dist(A, B):
    return math.pow(A[0] - B[0], 2) + math.pow(A[1] - B[1], 2)

def get_max_dist():
    cnt = len(arr)
    result = 0
    for i in range(cnt):
        for j in range(i+1, cnt):
            dist = get_pow_dist(arr[i], arr[j])
            result = max(result, dist)
    return result

arr = []
answer = 20001

def choose(idx, cnt):
    global answer

    if cnt >= M:
        max_dist = get_max_dist()
        answer = min(answer, max_dist)
        return
    if idx >= N:
        return
    
    arr.append(coord[idx])
    choose(idx+1, cnt+1)
    arr.pop()

    choose(idx+1, cnt)

choose(0, 0)
print(int(answer))