arr = list(map(int, input().split()))

max = arr[0]

for a in arr[1:]:
    if max < a: max = a

print(max)