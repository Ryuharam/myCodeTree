n, m = map(int, input().split())

d = []
t = []
for _ in range(n):
    direction, time = input().split()
    d.append(direction)
    t.append(int(time))

d2 = []
t2 = []
for _ in range(m):
    direction, time = input().split()
    d2.append(direction)
    t2.append(int(time))

def makeSim(d, t):
    res = [0] * (sum(t)+1)

    c = 0
    ct = 0

    for i in range(len(d)):
        for j in range(t[i]):
            ct += 1
            c = (c + 1) if d[i] =="R" else (c - 1)
            res[ct] = c

    return res

A = makeSim(d, t)

B = makeSim(d2, t2)

ans = -1
for i in range(len(A)):
    if A[i] != 0 and B[i]!= 0 and A[i] == B[i]:
        ans = i
        break

print(ans)
