m1, d1, m2, d2 = map(int, input().split())
A = input()

date = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
dates = [0 for _ in range(13)]
sum = 0
for i in range(1, 13):
    sum += date[i]
    dates[i] = sum

diff = (dates[m2-1]+d2) - (dates[m1-1]+d1)

day = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
idx = day.index(A)

print((diff - idx)//7 + 1)