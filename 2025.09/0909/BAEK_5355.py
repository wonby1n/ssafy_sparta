T = int(input())
for tc in range(1, T+1):
    arr = list(input().split())
    N = len(arr)
    num = float(arr[0])

    for i in range(1,N):
        if arr[i] == '@':
            num *= 3
        elif arr[i] == '%':
            num += 5
        elif arr[i] == '#':
            num -= 7

    print(f'{num:.2f}')
