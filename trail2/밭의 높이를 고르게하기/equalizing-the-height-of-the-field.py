N, H, T = map(int, input().split())
arr = list(map(int, input().split()))

price = [abs(arr[i] - H) for i in range(N)]

min_val = 20000

for i in range(N - T + 1):
    sum = 0
    for j in range(i, i + T):
        sum += price[j]
    min_val = min(min_val, sum)

print(min_val)