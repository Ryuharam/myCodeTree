a, b = input().split()

ab = ''.join((a, b))
ba = ''.join((b, a))

print(int(ab)+int(ba))