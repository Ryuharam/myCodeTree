N, K, P, T = map(int, input().split())
handshakes = [tuple(map(int, input().split())) for _ in range(T)]

handshakes.sort(key=lambda x: x[0])

times = [-1] * (N+1)
times[P] = K

for t, s, e in handshakes:
    if times[s] > 0 and times[e] > 0:
        times[s] -= 1
        times[e] -= 1
    elif times[s] > 0:
        times[s] -= 1
        if times[e] == -1:
            times[e] = K
    elif times[e] > 0:
        times[e] -= 1
        if times[s] == -1:
            times[s] = K

for t in times[1:]:
    print(0 if t==-1 else 1, end="")