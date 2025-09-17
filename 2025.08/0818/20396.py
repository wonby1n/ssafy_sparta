T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    # i,j는 M번 입력받으므로
    for _ in range(M):
        i, j = map(int, input().split())
        color = arr[i-1]

        for c in range(i-1, i-1+j):
            if 0 <= c < N:
                arr[c] = color

    print(f'#{tc}', *arr)
