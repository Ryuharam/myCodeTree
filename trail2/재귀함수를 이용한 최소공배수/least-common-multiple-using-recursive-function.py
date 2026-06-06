n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def gcd(a, b):
    if a < b:
        a, b = b, a

    if a%b==0:
        return b
    
    return gcd(b, a%b)

def lcm(i):
    if i == 0:
        return arr[i]

    tmp = lcm(i-1)
    
    return (arr[i] * tmp)//gcd(arr[i],tmp)

print(lcm(n-1))