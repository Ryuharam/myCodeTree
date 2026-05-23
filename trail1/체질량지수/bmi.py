def cal(h:int, w:int):
    return (10000 * w)//(h*h)
    
h, w = input().split()

h = int(h)
w = int(w)

b = cal(h, w)
print(b)
if b >= 25:
    print("Obesity")