n = int(input())
arr = list(input().split())

cnt = 0

for i in range(n-1, 0 , -1):
    for j in range(0, i):
        if arr[j] > arr[j+1]:
            cnt += 1
            arr[j], arr[j+1] = arr[j+1], arr[j]

print(cnt)