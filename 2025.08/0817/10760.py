T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 델타배열 상하좌우, 대각선까지 살피기
    # 착륙지 높이보다 낮은 지역이 4곳 이상이면 후보지
    max_val = 0

    for r in range(N):
        for c in range(M):
            now = arr[r][c]
            universe = 0
            universe2 = 0
            for dr, dc in [[-1,0],[1,0],[0,-1],[0,1]]:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < N and 0 <= nc < M:
                    if arr[r][c] > arr[nr][nc]:
                        universe += 1
            for dr, dc in [[-1,-1],[-1,1],[1,-1],[1,1]]:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < N and 0 <= nc < M:
                    if arr[r][c] > arr[nr][nc]:
                        universe2 += 1

            if (universe + universe2) >= 4:
                max_val += 1


    print(f'#{tc} {max_val}')