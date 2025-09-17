T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 델타배열

    # 구하고 싶은 값
    max_val = 0

    for r in range(N):
        for c in range(M):
            now = arr[r][c]
            for dr, dc in [[-1,0],[1,0],[0,-1],[0,1]]:
                nr = dr + r
                nc = dc + c
                if 0 <= nr < N and 0 <= nc < M:
                    now += arr[nr][nc]

            if max_val < now:
                max_val = now

    print(f'#{tc} {max_val}')