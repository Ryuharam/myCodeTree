n = int(input())
moves = [tuple(input().split()) for _ in range(n)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]

stoi = {'N':0, 'S':1, 'W':2, 'E':3}
dx = [0,0,-1,1]
dy = [1,-1,0,0]
x = 0
y = 0

for i in range(n):
    d = stoi[dir[i]]

    x = x + dx[d] * dist[i]
    y = y + dy[d] * dist[i]


print(x,y)