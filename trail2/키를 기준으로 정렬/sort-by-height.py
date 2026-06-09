n = int(input())

class Person:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

people = []

for _ in range(n):
    n_i, h_i, w_i = input().split()
    people.append(Person(n_i,int(h_i),int(w_i)))

people.sort(key=lambda p:p.height)

for p in people:
    print(f'{p.name} {p.height} {p.weight}')