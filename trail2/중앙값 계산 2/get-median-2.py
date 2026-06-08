n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
for i in range(0,n,2):
    tmp = sorted(arr[:i+1])
    print(tmp[(i+1)//2], end=" ")