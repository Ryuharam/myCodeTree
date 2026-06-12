n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

cnt = [0 for _ in range(201)]

for s, e in segments:
    s, e = s+100, e+100
    for i in range(s,e):
        cnt[i] += 1

max = 0

for c in cnt:
    if c > max:
        max = c

print(max)