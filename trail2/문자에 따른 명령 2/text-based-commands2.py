dirs = input()

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

x, y = 0, 0
d = 0

for dir in dirs:
    if dir == 'F':
        x = x + dx[d]
        y = y + dy[d]
    elif dir == 'L':
        d = (d+3) % 4
    else:
        d = (d+1) % 4

print(x,y)