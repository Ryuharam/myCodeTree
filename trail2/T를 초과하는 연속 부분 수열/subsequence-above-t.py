n, t = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
ans = 0
cnt = 0

for i in range(n):
    if arr[i] > t:
        cnt += 1
    else:
        ans = max(ans, cnt)
        cnt = 0

ans = max(ans, cnt)
print(ans)