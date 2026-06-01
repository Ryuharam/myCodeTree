line = input()
result = []

for l in line:
 

    if 'a' <= l and l <= 'z':
        result.append(chr(ord(l) - ord('a') + ord('A')))
    elif 'A' <= l and l <= 'Z':
        result.append(l)

print(''.join(result))