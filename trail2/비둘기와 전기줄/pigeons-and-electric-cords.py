N = int(input())
pigeon = {}
cnt = 0

for _ in range(N):
    p, pos = map(int, input().split())
    if p in pigeon and pigeon.get(p) != pos:
        cnt += 1
    pigeon[p] = pos

print(cnt)