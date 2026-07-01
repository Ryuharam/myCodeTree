n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

ans = 1_600_000_000

for i in range(n):
    max_x, min_x, max_y, min_y = 0, 40000, 0, 40000
    for j in range(n):
        if i == j:
            continue
        max_x = max(max_x, x[j])
        min_x = min(min_x, x[j])
        max_y = max(max_y, y[j])
        min_y = min(min_y, y[j])
    
    size = (max_x - min_x) * (max_y - min_y)
    ans = min(ans, size)

print(ans)