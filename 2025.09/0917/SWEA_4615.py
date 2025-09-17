T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    grid = [[0] * (N) for _ in range(N)]

    # 좌표 가운데에 돌 배치하기
    mid = N // 2
    grid[mid - 1][mid - 1] = 2
    grid[mid][mid] = 2
    grid[mid][mid - 1] = 1
    grid[mid - 1][mid] = 1

    # 상하좌우, 좌상,좌하,우상,우하
    dr = [-1, 1, 0, 0, -1, 1, -1, 1]
    dc = [0, 0, -1, 1, -1, -1, 1, 1]

    # 돌 뒤집는 거 입력받기
    for _ in range(M):
        r, c, color = map(int, input().split())
        # 0번은 없으므로
        r -= 1
        c -= 1
        grid[r][c] = color

        # 상하좌우 대각선 탐색하기
        for k in range(8):
            nr = r + dr[k]
            nc = c + dc[k]
            # 탐색하면서 다른거 있으면 다 집어넣는다
            change = []

            while True:
                # 1. 범위 벗어나면 종료
                if not (0 <= nr < N and 0 <= nc < N):
                    break

                # 2. 암것도 없으면 종료
                if grid[nr][nc] == 0:
                    break

                # 3. 같은 색 만나면 뒤집기
                if grid[nr][nc] == color:
                    for cr, cc in change:
                        grid[cr][cc] = color
                    break

                # 4. 색 다르면 목록에 담고 이동하기
                change.append((nr, nc))
                nr += dr[k]
                nc += dc[k]

    black = 0
    white = 0
    for row in grid:
        black += row.count(1)
        white += row.count(2)

    print(f'#{tc} {black} {white}')
