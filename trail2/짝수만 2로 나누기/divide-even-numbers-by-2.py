n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def change(n,arr):
    for i in range(n):
        if arr[i]%2==0:
            arr[i] = arr[i]//2

change(n,arr)

print(*arr)