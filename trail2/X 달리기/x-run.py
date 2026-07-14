X = int(input())

# Please write your code here.
v = 0
move = 0
time = 0

def accum(num):
    if num <= 1:
        return num
    return num * (num + 1) // 2

while move < X:
    time += 1
    v += 1

    while v > 1 and (move + accum(v)) > X:
        v -= 1
    
    move += v


print(time)
