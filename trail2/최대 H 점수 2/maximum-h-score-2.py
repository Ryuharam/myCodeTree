N, L = map(int, input().split())
a = list(map(int, input().split()))

max_val = 0

for h in range(1, max(a) + 1):
    cnt1 = 0
    cnt2 = 0
    for i in range(N):
        if a[i] >= h:
            cnt1 += 1
        elif a[i] == h - 1:
            cnt2 += 1
    
    if cnt1 >= h:
        max_val = max(max_val, h)
    elif L + cnt1 >= h and cnt2 + cnt1 >= h:
        max_val = max(max_val, h)

print(max_val)