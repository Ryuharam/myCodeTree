n = int(input())
times = [tuple(map(int, input().split())) for _ in range(n)]

max_val = 0

for i in range(n):
    # i번 개발자 해고
    work = [0 for _ in range(1001)]
    for j in range(n):
        for k in range(times[j][0], times[j][1]):
            if i == j:
                continue
            work[k] = 1

    max_val = max(max_val, sum(work))


print(max_val)