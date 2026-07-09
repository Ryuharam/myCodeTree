x1, x2, x3, x4 = map(int, input().split())

def isIn(x, a, b):
    return a <= x and x <= b

if isIn(x1, x3, x4) or isIn(x2, x3, x4) or isIn(x3, x1, x2) or isIn(x4, x1, x2):
    print("intersecting")
else:
    print("nonintersecting")