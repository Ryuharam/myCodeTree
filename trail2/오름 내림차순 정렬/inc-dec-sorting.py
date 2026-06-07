n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.
nums.sort()
for n in nums:
    print(n,end=" ")
print()

for n in nums[::-1]:
    print(n, end=" ")