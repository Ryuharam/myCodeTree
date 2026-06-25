N, S = map(int, input().split())
arr = list(map(int, input().split()))

sum = 0
for a in arr:
    sum += a

min_diff = S

for i in range(N):
    for j in range(i+1, N):
        tmp = sum - (arr[i] + arr[j])
        min_diff = min(min_diff, abs(S - tmp))

print(min_diff)

