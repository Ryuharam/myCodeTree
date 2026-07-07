n, m = map(int, input().split())
arr = [0] + list(map(int, input().split()))

max_val = 0

for i in range(1, n+1):
    st = i
    sum = 0
    for _ in range(m):
        sum += arr[st]
        st = arr[st]
    max_val = max(max_val, sum)

print(max_val)

