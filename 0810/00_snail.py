T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]

    x, y, d = 0, 0, 0
    dx = [0, 1, 0, -1]  # 오른쪽, 아래, 왼쪽, 위
    dy = [1, 0, -1, 0]

    for num in range(1, N * N + 1):
        arr[x][y] = num
        nx = x + dx[d]
        ny = y + dy[d]

        if nx < 0 or nx >= N or ny < 0 or ny >= N or arr[nx][ny] != 0:
            d = (d + 1) % 4
            nx = x + dx[d]
            ny = y + dy[d]

        x, y = nx, ny

    print(f"#{tc}")
    for row in arr:
        print(*row)