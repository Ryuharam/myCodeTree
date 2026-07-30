import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

cnt_even = 0
cnt_odd = 0

for a in arr:
    if a % 2 == 0:
        cnt_even += 1
    else:
        cnt_odd += 1

while cnt_odd > cnt_even:
    cnt_odd -= 2
    cnt_even += 1

if cnt_even == cnt_odd:
    print(cnt_even * 2)
else:  
    print(cnt_odd * 2 + 1)