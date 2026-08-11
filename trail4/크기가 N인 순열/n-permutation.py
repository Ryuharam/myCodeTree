N = int(input())

arr = []
used = [False for _ in range(N+1)]

def choose(idx: int):
    if idx >= N:
        print(*arr)
        return
    
    for i in range(1, N+1):
        if used[i]:
            continue
        
        arr.append(i)
        used[i] = True
        choose(idx + 1)
        arr.pop()
        used[i] = False

choose(0)