n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]
x1, x2 = zip(*segments)
x1, x2 = list(x1), list(x2)

def main():
    for i in range(n):
        for j in range(i+1, n):
            if x1[i] > x2[j] or x2[i] < x1[j]:
                print("No")
                return

    print("Yes")

main()