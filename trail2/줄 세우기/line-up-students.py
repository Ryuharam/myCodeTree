n = int(input())
students = [tuple(map(int, input().split())) + (i + 1,) for i in range(n)]

students.sort(key=lambda s: (-s[0], -s[1], s[2]))

for s in students:
    print(f'{s[0]} {s[1]} {s[2]}')
