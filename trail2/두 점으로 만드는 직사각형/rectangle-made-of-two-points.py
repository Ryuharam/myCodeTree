import sys

input = sys.stdin.readline

box1 = list(map(int, input().split()))
box2 = list(map(int, input().split()))

min_x = min(box1[0], box2[0])
min_y = min(box1[1], box2[1])
max_x = max(box1[2], box2[2])
max_y = max(box1[3], box2[3])

print((max_x - min_x) * (max_y - min_y))