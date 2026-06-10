n = int(input())
sequence = list(map(int, input().split()))

sorted_seq = sorted(sequence)

ans = [0 for _ in range(n)]
used = [False for _ in range(n)]

for i in range(n):
    for j in range(n):
        if sequence[i] == sorted_seq[j] and not used[j]:
            ans[i] = j+1
            used[j] = True
            break

print(*ans)
