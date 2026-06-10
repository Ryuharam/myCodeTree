n = int(input())
students = [
    (h, w, i + 1)
    for i, (h, w) in enumerate([tuple(map(int, input().split())) for _ in range(n)])
]

# Please write your code here.
students.sort(key=lambda x:(x[0], -x[1]))

for s in students:
    print(s[0],s[1],s[2])