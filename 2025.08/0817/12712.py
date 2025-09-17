T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split()) # M -> 세기
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 최대 잡을 수 있는 파리 수
    max_val = 0

    # 델타 상하좌우, 대각선
    delta1 = [[-1,0],[1,0],[0,-1],[0,1]]
    delta2 = [[1,1],[-1,-1],[-1,1],[1,-1]]

    for r in range(N):
        for c in range(N):
            now = arr[r][c]
            now2 = arr[r][c]

            # 분사 세기만큼 반복해서 곱해주기
            for k in range(1, M):
                # 상하좌우
                for dr, dc in delta1:
                    nr = r + dr * k
                    nc = c + dc * k
                    if 0 <= nr < N and 0 <= nc < N:
                        now += arr[nr][nc]

                # 대각선
                for dr2, dc2 in delta2:
                    nr2 = r + dr2 * k
                    nc2 = c + dc2 * k
                    if 0 <= nr2 < N and 0 <= nc2 < N:
                        now2 += arr[nr2][nc2]

            if max_val < now:
                max_val = now
            if max_val < now2:
                max_val = now2

    print(f'#{tc} {max_val}')