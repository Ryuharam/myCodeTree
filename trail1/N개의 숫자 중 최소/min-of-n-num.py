n = int(input())
a = list(map(int, input().split()))

# Please write your code here.
min = a[0]
cnt = 1

for num in a[1:]:
    if min > num:
        min = num
        cnt = 1
    elif min == num:
        cnt += 1

print(min, cnt)