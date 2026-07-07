N = int(input())
seat = input()

def get_min_val(s: str):
    global N
    min_diff = N
    for i in range(N):
        for j in range(i+1, N):
            if s[i] == "1" and s[j] == "1":
                min_diff = min(min_diff, j-i)
    return min_diff

max_val = 0
for i in range(N):
    if seat[i] == "0":
        tmp = seat[:i] + "1" + seat[i+1:]
        max_val = max(max_val, get_min_val(tmp))

print(max_val)