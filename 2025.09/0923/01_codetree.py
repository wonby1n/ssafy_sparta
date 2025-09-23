n, k = map(int, input().split())
arr = list(map(int, input().split()))

result = 0

for i in range(n-k+1):
    now_sum = 0
    for j in range(i,i+k):
        now_sum += arr[j]
    if result < now_sum:
        result = now_sum

print(result)
