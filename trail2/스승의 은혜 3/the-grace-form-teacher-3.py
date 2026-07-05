N, B = map(int, input().split())
gifts = [list(map(int, input().split())) for _ in range(N)]
P = [gift[0] for gift in gifts]
S = [gift[1] for gift in gifts]

max_cnt = 0

for i in range(N):
    gifts[i][0] //= 2

    sorted_gifts = sorted(gifts, key=lambda x: x[0] + x[1])
    sum_val = 0
    cnt = 0

    for j in range(N):
        sum_val += sum(sorted_gifts[j])

        if sum_val > B:
            max_cnt = max(max_cnt, cnt)
            break
        cnt += 1

    gifts[i][0] *= 2

print(max_cnt)