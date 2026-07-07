N, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]
 
max_cnt = 0

for a in range(1, 10001):
    b = a + K
    cnt = 0
    for n in arr:
        if a <= n and n <= b:
            cnt += 1
    max_cnt = max(max_cnt, cnt)

print(max_cnt)
