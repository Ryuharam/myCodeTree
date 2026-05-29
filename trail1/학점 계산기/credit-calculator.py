n = int(input())

score = map(float, input().split())

mean = round(sum(score)/n, 1)

print(mean)

if mean >= 4.0:
    print("Perfect")
elif mean >= 3.0:
    print("Good")
else:
    print("Poor")