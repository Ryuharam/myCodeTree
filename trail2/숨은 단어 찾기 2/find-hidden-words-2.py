N, M = map(int, input().split())
arr = [input() for _ in range(N)]

dr = [1, 0, -1, 0, 1, 1, -1, -1]
dc = [0, -1, 0, 1, 1, -1, 1, -1]

cnt = 0

for i in range(N):
    for j in range(M):
        if arr[i][j] == 'L':
            for d in range(8):
                nr1 = i + dr[d]
                nc1 = j + dc[d]

                nr2 = i + dr[d]*2
                nc2 = j + dc[d]*2

                if nr1>=0 and nr1<N and nc1>=0 and nc1<M and nr2>=0 and nr2<N and nc2>=0 and nc2<M and arr[nr1][nc1] == 'E' and arr[nr2][nc2] == 'E':
                    cnt += 1

print(cnt)