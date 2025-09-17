N = int(input())
arr = list(map(int, input().split()))

# 가장 큰 수와 가장 작은 수를 리스트 0번째로 가정
max_val = arr[0]
min_val = arr[0]

for i in range(N):
    if max_val < arr[i]:
        max_val = arr[i]
    if min_val < arr[i]:
        min_val = arr[i]

result = max_val - min_val

print(result)