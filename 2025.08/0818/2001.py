T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # max
    max_val = 0
    for r in range(N-M+1):
        for c in range(N-M+1):
            now = 0
            for i in range(M):
                for j in range(M):
                    now += arr[r+i][c+j]
            if max_val < now:
                max_val = now

    print(f'#{tc} {max_val}')