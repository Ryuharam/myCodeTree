N = int(input())
seats = list(map(int, list(input())))

max_diff = 0

def check(seats: list[str]):
    global max_diff

    min_diff = N
    l = -1
    for i in range(N):
        if seats[i] == 1:
            if l == -1:
                l = i
            else:
                min_diff = min(min_diff, i - l)
                l = i
    
    max_diff = max(min_diff, max_diff)

for i in range(N):
    if seats[i] == 1:
        continue
    seats[i] = 1
    check(seats)
    seats[i] = 0

print(max_diff)