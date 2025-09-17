N = int(input())
arr = [0] * 2
for _ in range(N):
    a = int(input())
    arr[a] += 1

if arr[0] > arr[1]:
    print('Junhee is not cute!')
else:
    print('Junhee is cute!')