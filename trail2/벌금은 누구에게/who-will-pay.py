N, M, K = map(int, input().split())
student = [int(input()) for _ in range(M)]

a = -1
cnt = [0] * (N+1)
for s in student:
    cnt[s] += 1
    if cnt[s] >= K:
        a = s
        break
print(a)
