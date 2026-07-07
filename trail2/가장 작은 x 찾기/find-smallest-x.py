n = int(input())
ranges = [tuple(map(int, input().split())) for _ in range(n)]
a, b = zip(*ranges)
a, b = list(a), list(b)

for s in range(1, 10001):
    curr = s
    flag = True
    for i in range(n):
        curr *= 2

        if a[i] > curr or b[i] < curr:
            flag = False
            break

    if flag:
        print(s)
        break
