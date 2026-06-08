n = int(input())
word = [input() for _ in range(n)]

# Please write your code here.
word.sort()

for w in word:
    print(w)