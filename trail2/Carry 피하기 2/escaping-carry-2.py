n = int(input())
arr = [int(input()) for _ in range(n)]

max_val = 0

def is_carry(left, right):
    l = str(left)
    r = str(right)

    for i in range(1, min(len(l), len(r))+1):
        if int(l[-i]) + int(r[-i]) >= 10:
            return True
    
    return False

for i in range(n):
    for j in range(i+1, n):
        if is_carry(arr[i], arr[j]):
            continue
        for k in range(j+1, n):
            if is_carry(arr[i] + arr[j], arr[k]):
                continue
            max_val = max(max_val, arr[i]+arr[j]+arr[k])

print(max_val if max_val != 0 else -1 )
            

