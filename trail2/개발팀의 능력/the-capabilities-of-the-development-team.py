arr = list(map(int, input().split()))


ans = 2000

for i in range(5):
    choosed = [False] * 5
    team1, team2, team3 = 0, 0, 0
    # team1
    team1 = arr[i]
    choosed[i] = True
    for j in range(5):
        if choosed[j]:
            continue
        choosed[j] = True
        for k in range(5):
            if choosed[k]:
                continue
            team2 = arr[j] + arr[k]
            team3 = sum(arr) - team1 - team2

            if team1 == team2 or team1 == team3 or team2 == team3:
                continue

            min_val = min(team1, min(team2, team3))
            max_val = max(team1, max(team2, team3))
            diff = max_val - min_val

            ans = min(ans, diff)
print(ans if ans!=2000 else -1)