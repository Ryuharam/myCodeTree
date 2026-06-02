n, m = map(int, input().split())

# Please write your code here.

def draw_box(n:int, m:int):
    for _ in range(n):
        print('1'*m)


draw_box(n,m)