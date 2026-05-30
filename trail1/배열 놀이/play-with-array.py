n, q = list(map(int, input().split()))

arr = list(map(int, input().split()))

for _ in range(q):
    tmp = input().split()
    o = int(tmp[0])

    if o==1:
        a = int(tmp[1])
        print(arr[a-1])
    elif o==2:
        b = int(tmp[1])
        if b not in arr:
            print(0)
        else:
            print(arr.index(b)+1)
    else:
        s = int(tmp[1])-1
        e = int(tmp[2])-1
        
        for i in range(s, e+1):
            print(arr[i],end=" ")
        print("")

        
