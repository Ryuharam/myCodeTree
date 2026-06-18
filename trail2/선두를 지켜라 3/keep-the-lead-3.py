N, M = map(int, input().split())

# Process A's movements
v = []
t = []
for _ in range(N):
    vi, ti = map(int, input().split())
    v.append(vi)
    t.append(ti)

# Process B's movements
v2 = []
t2 = []
for _ in range(M):
    vi, ti = map(int, input().split())
    v2.append(vi)
    t2.append(ti)

total_time = sum(t)
A = [0] * (total_time + 1)
time = 0
for i in range(N):
    for j in range(t[i]):
        time += 1
        A[time] = A[time - 1] + v[i]

B = [0] * (total_time + 1)
time = 0
for i in range(M):
    for j in range(t2[i]):
        time += 1
        B[time] = B[time-1] + v2[i]

cnt = 0
c = -1
for i in range(1,total_time+1):
    if A[i] > B[i] and c != 1:
        c = 1
        cnt += 1
    elif A[i] < B[i] and c != 2:
        c = 2
        cnt += 1
    elif A[i] == B[i] and c !=3:
        c = 3
        cnt += 1

print(cnt)
