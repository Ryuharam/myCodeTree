n1, n2 = list(map(int, input().split()))

a = list(map(int, input().split()))
b = list(map(int, input().split()))

flag = False

if b[0]in a and len(b) <= len(a):
    for i in range(len(a)):
        if b[0] == a[i]:
            for j in range(len(b)):
                if (i+j)<len(a) and b[j] == a[i+j]:
                    if j == len(b)-1:
                        flag = True

                else: break

print("Yes" if flag else "No")



