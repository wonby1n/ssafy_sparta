T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_val = 0
    for r in range(N):
        for c in range(M):
            now = arr[r][c]
            for k in range(1, now+1):
                for dr, dc in [[-1,0],[1,0],[0,-1],[0,1]]:
                    nr = r + dr * k
                    nc = c + dc * k
                    if 0 <= nr < N and 0 <= nc < M:
                        now += arr[nr][nc]

            if max_val < now:
                max_val = now

    print(f'#{tc} {max_val}')