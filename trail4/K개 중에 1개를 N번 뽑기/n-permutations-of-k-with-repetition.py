K, N = map(int, input().split())

# Please write your code here.
def choose(arr, idx):
    global K, N

    if idx == N:
        print(*arr)
        return
    
    for i in range(1, K+1):
        arr.append(i)
        choose(arr, idx+1)
        arr.pop()

choose([], 0)


