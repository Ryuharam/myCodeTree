a, b = tuple(map(int, input().split()))

c = a + b
c = str(c)
cnt = 0

for i in c:
    if i=='1':
        cnt += 1

print(cnt)