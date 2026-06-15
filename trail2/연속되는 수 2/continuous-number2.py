n = int(input())
arr = [int(input()) for _ in range(n)]

# Please write your code here.
max_cnt = 1
cnt = 1

for i in range(1,n):
    if arr[i-1] == arr[i]:
        cnt += 1
    else:
        max_cnt = max(max_cnt, cnt)
        cnt = 1

max_cnt = max(max_cnt, cnt)

print(max_cnt)
