n = int(input())
cnt = 1

for _ in range(n):
    for _ in range(n):
        print(cnt, end=" ")
        cnt += 1
    print()