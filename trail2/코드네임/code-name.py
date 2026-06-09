MAX_N = 5

codenames = []
scores = []
for _ in range(MAX_N):
    codename, score = input().split()
    codenames.append(codename)
    scores.append(int(score))

# Please write your code here.
class Agent:
    def __init__(self, codename:str, score:int):
        self.codename = codename
        self.score = score

    def __lt__(self, other):
        return self.score < other.score

    def __repr__(self):
        return(f'{self.codename} {self.score}')

agents = []
for name, score in zip(codenames, scores):
    agents.append(Agent(name, score))

agents.sort()
print(agents[0])