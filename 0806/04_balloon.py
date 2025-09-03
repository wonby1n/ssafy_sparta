# N -> 행 M -> 열

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 델타인가 머시긴가

    # 상하좌우 정해주기
    dr = [-1,1,0,0]
    dc = [0,0,-1,1]

    # 내가 구하고 싶은 최대 풍선
    max_val = 0

    for r in range(N): # 행부터 순회
        for c in range(M): # 열 순회
            flower = arr[r][c]  # 퍼지는 거리
            balloon = arr[r][c] # 풍선의 현재 위치

            # 현재 위치에서 상하좌우를 구함
            for k in range(4):
                for f in range(1, flower+1):
                    # 새로운 행(nr)은 현재위치(r)에서 dr[k]만큼 이동
                    nr = r + dr[k] * f
                    # 새로운 열(nc)은 현재위치(r)에서 dc[k]만큼 이동
                    nc = c + dc[k] * f
                    # 이걸 네번하면 상하좌우 구할 수 있음, 물론 아래 if 식으로 범위 벗어나면 안되게 해야 함
                    if 0 <= nr < N and 0 <= nc < M:
                        balloon += arr[nr][nc]

            if max_val < balloon:
                max_val = balloon

    print(f'#{tc} {max_val}')