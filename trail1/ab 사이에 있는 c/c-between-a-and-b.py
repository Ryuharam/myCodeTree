a,b,c = input().split()
a = int(a)
b = int(b)
c = int(c)

flag = False

for i in range(a, b+1):
    if i%c==0:
        flag = True
        break

if flag:
    print("YES")
else:
    print("NO")