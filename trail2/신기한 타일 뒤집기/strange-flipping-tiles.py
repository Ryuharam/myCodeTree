n = int(input())
commands = [tuple(input().split()) for _ in range(n)]
x = []
dir = []
for num, direction in commands:
    x.append(int(num))
    dir.append(direction)

# Please write your code here.

MAX_SIZE = 200005

state = ["G"] * MAX_SIZE
s = 100000

for i in range(n):
    if dir[i] == 'L':
        for j in range(x[i]):
            ns = s - j
            state[ns] = 'W'
        s = s - x[i] + 1
    else:
        for j in range(x[i]):
            ns = s + j
            state[ns] = 'B'
        s = s + x[i] - 1

w, b = 0,0
for s in state:
    if s == 'W':
        w += 1
    elif s == 'B':
        b += 1

print(w,b)