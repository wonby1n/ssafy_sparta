N = int(input())
arr = list(map(int, input().split()))

cnt = 0

# 각자 인덱스랑 값 비교하기
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if i < j < k and arr[i] <= arr[j] <= arr[k]:
                cnt += 1

print(cnt)