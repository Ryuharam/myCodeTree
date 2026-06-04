text = input()
pattern = input()

# Please write your code here.

def check():
    if pattern in text:
        return text.index(pattern)
    return -1

print(check())