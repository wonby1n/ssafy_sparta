n = int(input())
arr = [int(input()) for _ in range(n)]
result = 0
cnt = 1
if n > 1:
    for i in range(1, n):
        if arr[i] == arr[i-1]:
            cnt +=1
        else:
            result = max(result, cnt)
            cnt = 1
else:
    result = 1

result = max(result, cnt)

print(result)