import sys

A = list(input())
N = len(A)

if len(set(A)) == 1:
    ans = A[0] + str(len(A))
    print(len(ans))
    sys.exit()

while A[0] == A[-1]:
    tmp = A[-1]
    for i in range(N-1, 0, -1):
        A[i] = A[i-1]
    A[0] = tmp

ans = ""
cnt = 1
prev = A[0]
for i in range(1, N):
    if prev == A[i]:
        cnt += 1
    else:
        ans += prev + str(cnt)
        prev = A[i]
        cnt = 1

ans += prev + str(cnt)

print(len(ans))