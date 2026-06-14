expression = input()

alpha = []
for c in expression:
    if c.isalpha() and c not in alpha:
        alpha.append(c)

alpha_map = {}
max = -float('inf')

def cal():
    res = alpha_map[expression[0]]
    oper = None

    for i in range(1, len(expression)):
        c = expression[i]
        if c in ['+','-','*']:
            oper = c
        else:
            val = alpha_map[c]
            if oper =='+':
                res += val
            elif oper =='-':
                res -= val
            elif oper == '*':
                res *= val
    return res

def btk(idx):
    global max

    if idx == len(alpha):
        res = cal()
        if res > max:
            max = res
        return
    
    a = alpha[idx]
    for num in range(1, 5):
        alpha_map[a] = num
        btk(idx+1)

btk(0)
print(max)
