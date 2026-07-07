N = int(input())
string = input()

for i in range(1, N+1):
    # 길이 i
    list = []
    flag = True
    for j in range(N - i + 1):
        if string[j:j+i] in list:
            flag = False
            break
        else:
            list.append(string[j:j+i])
    if flag:
        print(i)
        break
