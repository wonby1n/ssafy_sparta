def recur(cnt, num):
    if len(num) == N:
        print(*num)
        return

    for i in range(N):
        if not used[i]:
            used[i] = 1
            recur(cnt+1, num+[arr[i]])
            used[i] = 0


N = int(input())
arr = []
for i in range(1, N+1):
    arr.append(i)

# 중복순열 제거 위한 used 배열 사용
used= [0] * (N+1)

recur(0,[])
print()