T = int(input())
for tc in range(1, T + 1):

    # 착륙지점 양옆대각선 8곳이 착륙지점보다 낮으면 ㅇㅋ
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for i in range(N)]

    # 일단 델타배열 때려넣어보자
    # 행 (세로)의 상하좌우 왼쪽위대 오른쪽위대 왼쪽밑대 오른쪽밑대
    dr = [-1,1,0,0,-1,-1,1,1]
    # 열 (가로)의 상하좌우 왼쪽위대 오른쪽위대 왼쪽밑대 오른쪽밑대
    dc = [0,0,-1,1,-1,1,-1,1]

    result = 0

    for r in range(N):
        for c in range(M):
            rocket = arr[r][c]

            for i in range(8):
                nr = r + dr[i]
                nc = c + dc[i]
                picture = []

                if 0 <= nr < N and 0 <= nc < M:
                    if arr[nr][nc] < rocket:
                        picture.append(arr[nr][nc])

                if len(picture) >= 4:
                    result += 1

    print(f'# {tc} {result}')