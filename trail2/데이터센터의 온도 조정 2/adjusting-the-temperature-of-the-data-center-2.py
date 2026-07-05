N, C, G, H = map(int, input().split())
ranges = [tuple(map(int, input().split())) for _ in range(N)]
t_a = [r[0] for r in ranges]
t_b = [r[1] for r in ranges]

min_val = min(t_a)
max_val = max(t_b)

def get_score(t_a: int, t_b: int, temp):
    global C, G, H
    if temp < t_a:
        return C
    if t_a <= temp and temp <= t_b:
        return G
    return H

max_scores = 0
for t in range(min_val-1, max_val+2):
    scores = 0
    for i in range(N):
        scores += get_score(ranges[i][0], ranges[i][1], t)
    max_scores = max(max_scores, scores)

print(max_scores)