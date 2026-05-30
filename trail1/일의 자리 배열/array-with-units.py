num = [0,0,0,0,0,0,0,0,0,0]

p,pp = input().split()
num[0] = int(p)
num[1] = int(pp)

for i in range(2, 10):
    num[i] = (num[i-1] + num[i-2]) % 10


for n in num:
    print(n,end=" ")