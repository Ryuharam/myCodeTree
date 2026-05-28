n = int(input())
a = 'A'
cnt = 0
for i in range(n):
    for j in range(n):
        print(chr(ord(a)+cnt), end="")
        cnt+=1
    print()