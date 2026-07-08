n, m = map(int, input().split())
a = list(map(int, input().split()))

l = max(a)
r = sum(a)

while l < r:
    # 구간 합들 중 최대값 mid
    mid = (l + r) // 2

    cnt = 0
    tmp = 0
    #print(f"시작 최솟값: {mid}, r: {r}, l: {l}")
    for i in range(n):
        tmp += a[i]

        if tmp > mid:
            tmp = a[i]
            cnt += 1
        #print(f"tmp: {tmp}, cnt: {cnt}")

    if tmp > 0:
        cnt += 1
    #print(f"나눠진 구간 수 : {cnt}, r: {r}, l: {l}")
    # 나눠진 구간 수
    if cnt > m:
        #print("너무 많이 나눠짐")
        # 너무 많이 나눠짐 -> mid 키우기
        l = mid + 1
    else:
        #print("적거나 적절히 나눠짐")
        # 정답 or 너무 적게 나눠짐
        r = mid

print(r)