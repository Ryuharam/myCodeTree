n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

ans = 0

def get_size(i, j, k):
    return abs((x[i]*y[j] + x[j]*y[k] + x[k]*y[i]) - (x[j]*y[i] + x[k]*y[j] + x[i]*y[k]))


for i in range(n):
    for j in range(n):
        for k in range(n):
            if i == j or j == k or k == i:
                continue
            if (x[i] == x[j] and x[k] != x[i] and (y[i] == y[k] or y[j] == y[k])) or (x[j] == x[k] and x[i] != x[j] and (y[i] == y[k] or y[i] == y[j])) or (x[k] == x[i] and x[i] != x[j] and (y[j] == y[k] or y[j] == y[i])):
                size = get_size(i,j,k)
                ans = max(ans, size)
print(ans)