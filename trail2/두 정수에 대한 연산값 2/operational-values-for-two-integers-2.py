a, b = map(int, input().split())

# Please write your code here.
def change(a, b):
    if a<b:
        return (a+10, b*2)
    else:
        return (a*2, b+10)

a, b = change(a, b)

print(a,b)