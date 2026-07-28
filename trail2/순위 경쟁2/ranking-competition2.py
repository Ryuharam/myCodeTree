import sys

input = sys.stdin.readline

n = int(input())

score = {'A' : 0, 'B' : 0}
cnt = 0
winner = ('A', 'B')

for _ in range(n):
    a, s = input().split()
    s = int(s)
    score[a] += s

    if score['A'] > score['B'] and winner != 'A':
        cnt += 1
        winner = 'A'
    elif score['A'] == score['B'] and winner != ('A','B'):
        cnt += 1
        winner = ('A','B')
    elif score['A'] < score['B'] and winner != 'B':
        cnt += 1
        winner = 'B'


print(cnt)    

