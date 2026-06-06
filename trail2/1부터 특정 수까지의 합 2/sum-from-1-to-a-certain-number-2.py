N = int(input())

# Please write your code here.

def fac(n):
    if n==1:
        return 1
    return n+fac(n-1)

print(fac(N))