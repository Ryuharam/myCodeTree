import sys

input = sys.stdin.readline

N = int(input())

arr = []

for _ in range(N):
    cmd = input().split()

    if cmd[0] == "push_back":
        arr.append(cmd[1])
    elif cmd[0] == "pop_back":
        arr.pop()
    elif cmd[0] == "size":
        print(len(arr))
    elif cmd[0] == "get":
        idx = int(cmd[1]) - 1
        print(arr[idx])