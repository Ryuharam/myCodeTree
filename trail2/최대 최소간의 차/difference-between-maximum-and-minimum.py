n, k = map(int, input().split())
arr = list(map(int, input().split()))

min_val = 1_000_000
for a in range(min(arr), 10001):
    price = 0
    b = a + k

    for i in range(n):
        if arr[i] < a:
            price += a - arr[i]
        elif arr[i] > b:
            price += arr[i] - b
    
    min_val = min(min_val, price)

print(min_val)