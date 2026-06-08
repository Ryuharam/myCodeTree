n, k, t = input().split()
n, k = int(n), int(k)
str = [input() for _ in range(n)]

# Please write your code here.
str.sort()
for idx in range(n):
    if str[idx].startswith(t):
        print(str[idx+k-1])
        break