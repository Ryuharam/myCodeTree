import sys

input = sys.stdin.readline

N, M, T = list(map(int, input().split()))

dr = [-1,1,0,0]
dc = [0,0,-1,1]
dir_dict = {"U":0, "D":1, "L":2, "R":3}
change_dir = {0:1, 1:0, 2:3, 3:2}

balls = []

def is_in(r, c):
    return 0 <= r and r < N and 0 <= c and c < N

for i in range(M):
    r, c, d, w = input().split()
    balls.append([i, int(r) - 1, int(c) - 1, dir_dict.get(d) , int(w)])

for t in range(T):
    tmp = [[[] for _ in range(N)] for _ in range(N)]

    for ball in balls:
        i, r, c, d, w = ball
        nr = r + dr[d]
        nc = c + dc[d]

        if is_in(nr, nc):
            # 이동
            tmp[nr][nc].append([i, d, w])
        else:
            # 방향 전환
            d = change_dir.get(d)
            tmp[r][c].append([i, d, w])
    
    balls = []
    for r in range(N):
        for c in range(N):
            if not tmp[r][c]:
                continue
            sum_w = 0
            for t in tmp[r][c]:
                sum_w += t[2]
            sorted_tmp = sorted(tmp[r][c], key=lambda x: -x[0])
            i = sorted_tmp[0][0]
            d = sorted_tmp[0][1]
            balls.append([i,r,c,d,sum_w])

ball_cnt = len(balls)
max_weight = 0
for b in balls:
    max_weight = max(max_weight, b[4])

print(ball_cnt, max_weight)
