n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]
x1 = [seg[0] for seg in segments]
x2 = [seg[1] for seg in segments]

def main():
    for i in range(n):
        flag = True
        for j in range(n):
            if i == j:
                continue
            for k in range(j+1, n):
                if k == i:
                    continue
                if x1[j] > x2[k] or x2[j] < x1[k]:
                    flag = False
                    break
            if not flag:
                break
        if flag:
            print("Yes")
            return
    print("No")

main()