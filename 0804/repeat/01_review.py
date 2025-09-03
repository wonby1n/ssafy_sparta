N = int(input())
arr = list(map(int, input().split()))

max_val = arr[0]
min_val = arr[0]

for i in range(1, N):
    if max_val < arr[i]:
        max_val = arr[i]
    if min_val > arr[i]:
        min_val = arr[i]

print(max_val - min_val)