import sys

input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

min = min(nums)
ans = max(nums)

if min == ans:
    print(-1)
    sys.exit()

ans += 1
idx = -1

for i in range(N):
    if nums[i] < ans and min != nums[i]:
        ans = nums[i]
        idx = i + 1
    elif nums[i] == ans and min != nums[i]:
        idx = -1

print(idx)