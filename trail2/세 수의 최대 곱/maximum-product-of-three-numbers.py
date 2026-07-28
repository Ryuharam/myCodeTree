import sys

input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

plus = []
minus = []

for n in nums:
    if n >= 0:
        plus.append(n)
    else:
        minus.append(n)

plus.sort()
minus.sort()

ans = -1000000000
# + + + 최대
if len(plus) >= 3:
    ans = max(ans, plus[-1]*plus[-2]*plus[-3])

# - - + 최대
if len(plus) >= 1 and len(minus) >= 2:
    ans = max(ans, plus[-1]*minus[0]*minus[1])

# + + -, - - - 최소
if len(plus) >= 2 and len(minus) >= 1:
    ans = max(ans, plus[0] * plus[1] * minus[-1])

if len(minus) >= 3:
    ans = max(ans, minus[-1]*minus[-2]*minus[-3])

print(ans)