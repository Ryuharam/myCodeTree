a, b, c, d = map(int, input().split())
ans = 0

# Please write your code here.
while True:
    if a==c and b==d:
        break
    b += 1
    ans += 1

    if b==60:
        a += 1
        b = 0

print(ans)