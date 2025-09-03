T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 구하고 싶은 값
    max_val = 0

    # 델타배열 상하좌우
    delta = [[-1,0],[1,0],[0,-1],[0,1]]

    for r in range(N):
        for c in range(N):
            # 중심이 될 현재 값 잡아주고
            now = arr[r][c]
            for k in range(1, N):
                for dr, dc in delta:
                    nr = r + dr * k
                    nc = c + dc * k
                    if 0 <= nr < N and 0 <= nc < N:
                        now += arr[nr][nc]
            if max_val < now:
                max_val = now

    print(f'#{tc} {max_val}')