import sys

n, m, p = map(int, input().split())
messages = [tuple(input().split()) for _ in range(m)]

if int(messages[p-1][1]) == 0:
    sys.exit()

people = set()
for i in range(n):
    people.add(chr(ord('A') + i))

for i in range(p-1, m):
    if messages[i][0] in people:
        people.remove(messages[i][0])

for i in range(p-2, -1, -1):
    if messages[p-1][1] == messages[i][1] and messages[i][0] in people:
        people.remove(messages[i][0])

print(*sorted(people))

    