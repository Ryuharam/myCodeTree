a, b = map(int, input().split())

# Please write your code here.

def ismult3(n: int) -> bool:
    return n%3==0

def ishave369(n: int) -> bool:
    line = str(n)
    for i in line:
        if i=='3' or i=='6' or i=='9':
            return True

    return False

cnt = 0

for i in range(a, b+1):
    if ismult3(i) or ishave369(i):
        cnt += 1

print(cnt)