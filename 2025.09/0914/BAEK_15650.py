def recur(cnt, num):
    if len(num) == M:
        print(*num)
        return

    for i in range(cnt, N):
        recur(i+1, num + [arr[i]])


N, M = map(int, input().split())
arr = []
for i in range(1, N+1):
    arr.append(i)

recur(0,[])
print()