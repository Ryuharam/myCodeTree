n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

move = 0
for i in range(n - 1):
    diff = A[i] - B[i]
    move += diff
    A[i + 1] += diff

print(move)

