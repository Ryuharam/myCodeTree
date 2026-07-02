N, B = map(int, input().split())
P = [int(input()) for _ in range(N)]

P = sorted(P)

cnt = 0
sum = 0
for i in P:
    sum += i
    cnt += 1

    if sum > B:
        sum -= i // 2
        if sum > B:
            print(cnt - 1)
        else:
            print(cnt)
        break
