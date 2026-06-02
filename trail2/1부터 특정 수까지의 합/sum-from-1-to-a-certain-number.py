n = int(input())

# Please write your code here.
def fun(n:int):
    res = 0
    for i in range(1,n+1):
        res += i
    
    return res//10

print(fun(n))