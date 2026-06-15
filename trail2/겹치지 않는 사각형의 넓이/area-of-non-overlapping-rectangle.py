x1 = [0] * 3
y1 = [0] * 3
x2 = [0] * 3
y2 = [0] * 3

x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())
x1[2], y1[2], x2[2], y2[2] = map(int, input().split())

# Please write your code here.
A = (x2[0] - x1[0]) * (y2[0] - y1[0])
B = (x2[1] - x1[1]) * (y2[1] - y1[1])

sum = A + B

for i in range(2):
    overlap_x = (min(x2[i], x2[2]) - max(x1[i], x1[2]))
    overlap_y = (min(y2[i], y2[2]) - max(y1[i], y1[2]))
    if overlap_x > 0 and overlap_y > 0:
        sum -= overlap_x * overlap_y

print(sum)
