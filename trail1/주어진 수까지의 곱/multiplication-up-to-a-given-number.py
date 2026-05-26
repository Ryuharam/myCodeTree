a, b = input().split()

r = 1

for i in range(int(a),int(b)+1):
    r *= i

print(r)