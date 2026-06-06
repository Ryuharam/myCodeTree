N = int(input())

# Please write your code here.

def cal(n):
    if n <= 1:
        return 0
    if n%2==0:
        return cal(n//2) + 1
    else:
        return cal(n//3) + 1

print(cal(N))