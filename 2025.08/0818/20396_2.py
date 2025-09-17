T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    for _ in range(M):
        i, j = map(int, input().split())
        # 일단 변경할 컬러를 지정
        color = arr[i-1]

        for r in range(i-1, i-1+j):
            if 0 <= r < N:
                arr[r] = color

    print(f'#{tc}', *arr)