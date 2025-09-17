N, T = map(int, input().split())
arr =list(map(int, input().split()))

idx = 0
num = 0
# T가 0이 되거나 0보다 작아질때까지
while T >= 0:
    T -= arr[idx]
    if T > 0:
        idx += 1
        num += 1
    else:
        T += arr[idx]
        break

print(num)