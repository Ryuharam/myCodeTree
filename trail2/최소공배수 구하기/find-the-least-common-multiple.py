import math

n, m = map(int, input().split())

# Please write your code here.

def 최소공배수(n:int, m:int) -> int:
    
    return (n*m)//math.gcd(n,m)

print(최소공배수(n,m))