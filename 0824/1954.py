T = int(input())
for tc in range(1, T+1):
    N = int(input())
    box = [[0] * N for _ in range(N)]

    # 델타 ? 우 -> 하 -> 좌 -> 상
    delta = [[0,1],[1,0],[0,-1],[-1,0]]
    # 현재 좌표
    r = 0
    c = 0
    d = 0

    for num in range(1, N*N+1):
        # 현재 좌표에 num 넣기
        box[r][c] = num

        # 새로운 좌표는 현재 좌표 더하기 델타 우하좌상
        nr = r + delta[d][0]
        nc = c + delta[d][1]

        # 범위 밖이고 이미 채워진 거면 이동시켜야함
        if not (0 <= nr < N and 0 <= nc < N and box[nr][nc] == 0):
            # 시계방향 공식
            d = (d+1) % 4
            nr = r + delta[d][0]
            nc = c + delta[d][1]
        # 다음 좌표로 이동하기
        r, c = nr, nc

    print(f'#{tc}')
    for row in box:
        print(*row)