N = int(input())
arr = []

for _ in range(N):
    arr.append(int(input()))

mean = sum(arr) // N

diff = 0

for i in range(N):
    diff += abs(arr[i] - mean)

print(diff // 2)
