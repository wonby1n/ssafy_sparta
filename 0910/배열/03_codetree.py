n = int(input())
arr = list(map(int, input().split()))

count = [0] * 9

for i in range(n):
    a = arr[i]-1
    count[a] += 1

for j in count:
    print(j)