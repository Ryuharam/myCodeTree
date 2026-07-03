N, M, D, S = map(int, input().split())

# 1. 사람 -> 치즈, 최초 먹은 시간
eat_records = {i: {} for i in range(1, N+1)}
for _ in range(D):
    person, milk, time = map(int, input().split())
    if milk not in eat_records[person]:
        eat_records[person][milk] = time
    else:
        eat_records[person][milk] = min(eat_records[person][milk], time)
    
# 사람 -> 아픈 시간
sick_people = {}
for _ in range(S):
    person, time = map(int, input().split())
    sick_people[person] = time

suspect_cheese = []

for c in range(1, M+1):
    is_suspect = True

    # 아픈 모든 사람들이 아프기 전에 이 치즈를 먹었는가
    for sp, sick_time in sick_people.items():
        if c not in eat_records[sp] or eat_records[sp][c] >= sick_time:
            is_suspect = False
            break
    
    if is_suspect:
        suspect_cheese.append(c)

maybe_sick = set()

for c in suspect_cheese:
    for p in range(1, N+1):
        if c in eat_records[p]:
            maybe_sick.add(p)
            

print(len(maybe_sick))