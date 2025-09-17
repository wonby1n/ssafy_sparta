T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    min_val = arr[0]
    max_val = arr[0]
    for i in range(1, N):
        if max_val < arr[i]:
            max_val = arr[i]
        elif min_val > arr[i]:
            min_val = arr[i]

    result = max_val - min_val

    print(f'#{test_case} {result}')