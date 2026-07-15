N = int(input())
seats = input()

l, r, p = 0, 0, 0

min_diff = N
max_diff = 0

for i in range(1, N):
    if seats[i] == '1':
        diff = i - p
        if max_diff < diff:
            max_diff = diff
            l = p
            r = i
        if min_diff > diff:
            min_diff = diff
        p = i


max_tmp = 0
for i in range(l + 1, r):
    max_tmp = max(max_tmp, min(i-l, r-i))

print(min(min_diff, max_tmp))

