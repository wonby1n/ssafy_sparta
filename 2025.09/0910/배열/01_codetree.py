n = int(input())
arr = [1, n]


for i in range(2,100):
    arr.append(arr[-1] + arr[-2])
    if arr[-1] >= 100:
        break

print(*arr)