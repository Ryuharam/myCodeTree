N = int(input())

# Please write your code here.
def cal(n):
    if n<10:
        return n*n
    return cal(n//10) + (n%10)*(n%10)

print(cal(N))