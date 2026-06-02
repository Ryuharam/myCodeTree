a, b, c = map(int, input().split())

# Please write your code here.

def get_min(a:int, b:int, c:int) -> int:
    return min(min(a,b),c)

print(get_min(a,b,c))