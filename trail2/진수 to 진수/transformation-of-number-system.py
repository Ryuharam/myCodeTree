a, b = map(int, input().split())
n = input()


ten = 0
for i in n:
    ten = ten * a + int(i)

digit = []
while True:
    if ten < b:
        digit.append(ten)
        break
    
    digit.append(ten%b)
    ten //= b

for d in digit[::-1]:
    print(d,end="")
