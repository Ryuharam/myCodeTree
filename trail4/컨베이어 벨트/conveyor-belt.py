import sys

input = sys.stdin.readline

N, T = list(map(int, input().split()))

arr1 = list(input().split())
arr2 = list(input().split())
arr2.reverse()

for _ in range(T):
    tmp1 = arr1[-1]
    for i in range(N-1, 0, -1):
        arr1[i] = arr1[i-1]
    tmp2 = arr2[0]
    for i in range(0, N-1):
        arr2[i] = arr2[i+1] 
    arr2[-1] = tmp1
    arr1[0] = tmp2


print(*arr1)
arr2.reverse()
print(*arr2)
