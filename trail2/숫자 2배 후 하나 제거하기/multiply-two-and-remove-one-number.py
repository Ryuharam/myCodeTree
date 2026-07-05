n = int(input())
arr = list(map(int, input().split()))

min_diff = 10000

for i in range(n):
    arr[i] *= 2
    for j in range(n):
        new_arr = [elem for idx, elem in enumerate(arr) if idx != j]

        sum_diff = 0
        for k in range(n - 2):
            sum_diff += abs(new_arr[k] - new_arr[k+1])

        min_diff = min(min_diff, sum_diff)
    arr[i] //= 2

print(min_diff)      