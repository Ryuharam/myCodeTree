n = int(input())

digit = []

while True:
    if n <= 1:
        digit.append(n)
        break

    digit.append(n%2)
    n //= 2

for d in digit[::-1]:
    print(d,end="") 