arr = ["apple","banana","grape","blueberry","orange"]

word = input()
cnt = 0

for a in arr:
    if a[2] == word or a[3] == word:
        print(a)
        cnt += 1
print(cnt)