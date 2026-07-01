arr = list(map(int, input().split()))

ans = 2000000

for i in range(6):
    for j in range(6):
        for k in range(6):
            for l in range(6):
                if i!=j and i!=k and i!=l and j!=k and j!=l and k!=l:
                    team1 = arr[i] + arr[j]
                    team2 = arr[k] + arr[l]
                    team3 = sum(arr) - team1 - team2
                    diff = max(team1, max(team2, team3)) - min(team1, min(team2, team3))
                    ans = min(ans, diff)

print(ans)