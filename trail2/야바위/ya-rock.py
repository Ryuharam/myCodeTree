n = int(input())
moves = [tuple(map(int, input().split())) for _ in range(n)]
a, b, c = zip(*moves)

max_point = 0

for i in range(1, 4):
    # i번 종이컵에 조약돌
    cup = [0] * 4
    cup[i] = 1
    point = 0
    for a, b, c in moves:
        cup[a], cup[b] = cup[b], cup[a]
        if cup[c] == 1:
            point += 1
    
    max_point = max(max_point, point)

print(max_point)