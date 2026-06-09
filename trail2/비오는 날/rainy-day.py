n = int(input())

class Pred:
    def __init__(self, date, day, weather):
        self.date = date
        self.day = day
        self.weather = weather
    
    def __lt__(self, other):
        return self.date < other.date

    def __repr__(self):
        return f'{self.date} {self.day} {self.weather}'

predicts = []

for _ in range(n):
    d, dy, w = input().split()
    predicts.append(Pred(d, dy, w))

predicts.sort()

for p in predicts:
    if p.weather == 'Rain':
        print(p)
        break