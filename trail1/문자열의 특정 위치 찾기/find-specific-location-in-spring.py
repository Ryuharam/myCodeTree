line, word = input().split()

if word in line:
    print(line.index(word))
else:
    print('No')