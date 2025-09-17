N = int(input())
arr = [int(input()) for _ in range(N)]

cnt = 1
result = 1

for i in range(1, N):
    # 같은 부호일 때만 연속 인정
    if (arr[i] > 0 and arr[i - 1] > 0) or (arr[i] < 0 and arr[i - 1] < 0):
        cnt += 1
    else:
        result = max(result, cnt)
        cnt = 1

result = max(result, cnt)
print(result)