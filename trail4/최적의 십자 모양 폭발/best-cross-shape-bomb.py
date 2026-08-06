import sys
import copy
from collections import deque

input = sys.stdin.readline

# 폭탄 위치 정하기
# 폭탄 터트리기
# 중력 작용
# 조건 만족하는 쌍의 개수 구하기 -> max

N = int(input())

board = [list(map(int, input().split())) for _ in range(N)]

max_cnt = 0

# 상, 하, 좌, 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 범위 체크
def is_in(r: int, c: int):
    return 0 <= r and r < N and 0 <= c and c < N

# 중력 작용
def gravity(board: list):
    dq = deque()
    for c in range(N):
        for i in range(N-1, -1, -1):
            if board[i][c] == 0:
                continue
            dq.append(board[i][c])
        for i in range(N-1, -1, -1):
            if not dq:
                board[i][c] = 0
            else:
                board[i][c] = dq.popleft()
    

# 쌍 개수 구하기
def get_pair(tmp: list):
    global max_cnt
    cnt = 0
    
    for r in range(N):
        for c in range(N):
            for d in range(4):
                nr = r + dr[d]
                nc = c + dc[d]

                if is_in(nr, nc) and tmp[r][c] != 0 and tmp[r][c] == tmp[nr][nc]:
                    cnt += 1
    max_cnt = max(max_cnt, cnt // 2)

for r in range(N):
    for c in range(N):
        # (r,c) 폭탄 터짐
        tmp = copy.deepcopy(board)
        size = tmp[r][c] - 1
        tmp[r][c] = 0

        for d in range(4):
            nr = r
            nc = c
            for s in range(size):
                nr = nr + dr[d]
                nc = nc + dc[d]

                if is_in(nr, nc):
                    tmp[nr][nc] = 0

        # 중력 작용
        gravity(tmp)

        # 쌍 찾기
        get_pair(tmp)


print(max_cnt)