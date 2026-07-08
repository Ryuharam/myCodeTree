n, k = map(int, input().split())
arr = list(map(int, input().split()))

def is_possible(max_val):
    step = []
    for i, a in enumerate(arr):
        if max_val >= a:
            step.append(i)
    
    for i in range(1, len(step)):
        diff = step[i] - step[i-1]
        if diff > k:
            return False
    return True

for i in range(max(arr[0], arr[-1]), 101):
    if is_possible(i):
        print(i)
        break