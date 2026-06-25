A = input()
n = len(A)
sum = 0

for i in range(n):
    if A[i] == '(':
        for j in range(i+1, n):
            if A[j] == ')':
                sum += 1

print(sum)