n, m = map(int, input().split())

# Please write your code here.
arr = [[0 for _ in range(m)] for _ in range(n)]

cnt = 1


for sum in range(max(n,m)*2):
    for j in range(sum+1):
        if j<n and (sum-j)<m:
            arr[j][sum-j] = cnt
            cnt += 1

for row in arr:
    for c in row:
        print(c,end=" ")
    print()
        