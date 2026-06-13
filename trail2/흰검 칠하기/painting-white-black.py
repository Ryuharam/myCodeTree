n = int(input())
commands = [tuple(input().split()) for _ in range(n)]
x = []
dir = []
for num, direction in commands:
    x.append(int(num))
    dir.append(direction)

MAX_SIZE = 200005
cnt_w = [0] * MAX_SIZE
cnt_b = [0] * MAX_SIZE
is_g = [0] * MAX_SIZE
color_state = ["X"] * MAX_SIZE

s = 100000

for i in range(n):
    if dir[i] == "L":
        for j in range(x[i]):  
            ns = s - j
            if is_g[ns] == 0:
                cnt_w[ns] += 1
                color_state[ns] = "W"
                if(cnt_w[ns] >= 2 and cnt_b[ns] >= 2):
                    is_g[ns] += 1
                    color_state[ns] = "G"

        s = s - x[i] + 1
    else:
        for j in range(x[i]):
            ns = s + j
            if is_g[ns] == 0:
                cnt_b[ns] += 1
                color_state[ns] = "B"
                if cnt_w[ns] >= 2 and cnt_b[ns] >= 2:
                    is_g[ns] += 1
                    color_state[ns] = "G"
        s = s + x[i] - 1

color = [0,0,0]
for i in range(MAX_SIZE):
    if(color_state[i] == "G"):
        color[2] += 1
    elif(color_state[i] == "W"):
        color[0] += 1
    elif(color_state[i] == "B"):
        color[1] += 1

print(*color)
        
