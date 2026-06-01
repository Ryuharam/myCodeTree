word = input()

line = list(word)

line.pop(1)
line.pop(-2)

print(''.join(line))