T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    max_val = -1
    max_idx = 0
    min_val = 99999999999
    min_idx = 0

    for i in range(N):
        if max_val <= arr[i]:
            max_val = arr[i]
            max_idx = i
        if min_val > arr[i]:
            min_val = arr[i]
            min_idx = i

    result = abs(max_idx-min_idx)

    print(f'#{tc} {result}')