n, m = map(int, input().split())
pairs = [tuple(map(int, input().split())) for _ in range(m)]

max_cnt = 0

for a in range(1, 11):
    for b in range(a + 1, 11):
        #print(f"a, b = {a}, {b} -> {pairs.count((a,b))} {pairs.count((b,a))}")
        cnt = pairs.count((a, b)) + pairs.count((b, a))
        max_cnt = max(max_cnt, cnt)

print(max_cnt)
    