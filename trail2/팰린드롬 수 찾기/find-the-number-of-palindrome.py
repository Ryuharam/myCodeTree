X, Y = map(int, input().split())

def ispalin(x):
    n = len(x)
    for i in range(n):
        if x[i] != x[n - i - 1]:
            return False
    return True

cnt = 0
for i in range(X, Y+1):
    if ispalin(str(i)):
        cnt += 1

print(cnt)