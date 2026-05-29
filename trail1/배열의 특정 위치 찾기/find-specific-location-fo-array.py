num = list(map(int, input().split()))

even = sum(num[1::2])
three = num[2::3]

print(even, round(sum(three)/len(three),1))