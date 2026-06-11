m1, d1, m2, d2 = map(int, input().split())

# Please write your code here.
days = [0,31,28,31,30,31,30,31,31,30,31,30,31]
sum_days = [0 for _ in range(13)]
sum = 0
for i in range(13):
    sum += days[i]
    sum_days[i] = sum

date = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

day1 = sum_days[m1-1] + d1
day2 = sum_days[m2-1] + d2

if day1 > day2:
    diff = day1 - day2
    print(date[-diff%7])
else:
    diff = day2 - day1
    print(date[diff%7]) 
