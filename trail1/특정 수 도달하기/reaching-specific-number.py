sum = 0
cnt = 0

num = input().split()

for n in num:
    n = int(n)

    if n >= 250:
        break

    sum += n
    cnt += 1

mean = sum/cnt

print(f'{sum} {mean:.1f}')