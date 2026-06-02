n = int(input())

# Please write your code here.
def check(n:int) -> bool:
    sum = 0
    for c in str(n):
        sum += int(c)

    return n%2==0 and sum %5==0

print('Yes' if check(n) else 'No')