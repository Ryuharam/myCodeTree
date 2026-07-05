X, Y = map(int, input().split())

max_val = 0

for i in range(X, Y+1):
    sum_val = sum(map(int, list(str(i))))
    max_val = max(max_val, sum_val)

print(max_val)