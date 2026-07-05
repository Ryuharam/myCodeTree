K, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(K)]

ability = [[] for _ in range(K)]
for i in range(K):
    for j in range(N):
        for k in range(j+1, N):
            ability[i].append((arr[i][j], arr[i][k]))

tmp = set(ability[0])

for i in range(1, K):
    tmp = tmp & set(ability[i])

print(len(tmp))
    