n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
def sum(s, e):
    sum = 0;
    for i in range(s-1, e):
        sum += arr[i]
    return sum

for i in range(m):
    print(sum(queries[i][0], queries[i][1]))