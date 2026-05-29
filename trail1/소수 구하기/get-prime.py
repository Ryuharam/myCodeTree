n = int(input())

list = []

for i in range(2, n+1):
    list.append(i)

for i in range(2, n+1):
    for j in range(2, i):
        if i%j==0 and i in list:
            list.remove(i)

for i in list:
    print(i,end=" ")