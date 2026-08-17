import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

if sum(arr) % 2 != 0:
    print("No")
    sys.exit()

sum_val = sum(arr)
mid = sum_val // 2

bag = [0]

for i in range(N):
    for b in bag:
        tmp = b + arr[i]
        if tmp == mid:
            print("Yes")
            sys.exit()
        elif tmp < mid:
            bag.append(tmp)

print("No")