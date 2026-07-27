N = int(input())
moves = [tuple(map(int, input().split())) for _ in range(N)]
a, b = zip(*moves)
a, b = list(a), list(b)

max_win = 0

# case1 - 1: 가위, 2: 바위, 3: 보 인 경우
# case2 - 1: 가위, 2: 보, 3: 바위
# case3 - 1: 바위, 2: 가위, 3: 보
# case4 - 1: 바위, 2: 보, 3: 가위
# case5 - 1: 보, 2: 가위, 3: 바위
# case6 - 1: 보, 2: 바위, 3: 가위

cnts = [0 for _ in range(6)]
for i in range(N):
    if a[i] == 1:
        if b[i] == 2:
            cnts[1] += 1
            cnts[2] += 1
            cnts[5] += 1
        elif b[i] == 3:
            cnts[0] += 1
            cnts[3] += 1
            cnts[4] += 1
    elif a[i] == 2:
        if b[i] == 1:
            cnts[0] += 1
            cnts[3] += 1
            cnts[4] += 1
        elif b[i] == 3:
            cnts[1] += 1
            cnts[2] += 1
            cnts[5] += 1
    elif a[i] == 3:
        if b[i] == 1:
            cnts[1] += 1
            cnts[2] += 1
            cnts[5] += 1
        elif b[i] == 2:
            cnts[0] += 1
            cnts[3] += 1
            cnts[4] += 1


print(max(cnts))
