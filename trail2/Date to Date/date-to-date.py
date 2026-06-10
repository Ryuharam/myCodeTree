m1, d1, m2, d2 = map(int, input().split())

# Please write your code here.
days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
sum_days = [0 for _ in range(13)]

sum = 0
for i in range(13):
    sum += days[i]
    sum_days[i] = sum

ans = (sum_days[m2 - 1] + d2) - (sum_days[m1 - 1] + d1) + 1
print(ans)
