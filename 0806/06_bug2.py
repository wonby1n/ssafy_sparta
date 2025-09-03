# N X N 배열
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 상하좌우 델타 (+ 모양)
    dr_plus = [-1, 1, 0, 0]
    dc_plus = [0, 0, -1, 1]

    # 대각선 델타 (x 모양)
    dr_cross = [-1, -1, 1, 1]
    dc_cross = [-1, 1, -1, 1]

    max_val = 0

    for r in range(N):
        for c in range(N):
            # 중심 값
            plus_sum = arr[r][c]
            cross_sum = arr[r][c]

            # + 모양 계산
            for k in range(4):
                for s in range(1, M):  # 1칸부터 M-1칸까지
                    nr = r + dr_plus[k] * s
                    nc = c + dc_plus[k] * s
                    if 0 <= nr < N and 0 <= nc < N:
                        plus_sum += arr[nr][nc]

            # × 모양 계산
            for k in range(4):
                for s in range(1, M):
                    nr = r + dr_cross[k] * s
                    nc = c + dc_cross[k] * s
                    if 0 <= nr < N and 0 <= nc < N:
                        cross_sum += arr[nr][nc]

            # 두 모양 중 큰 값을 비교
            local_max = plus_sum
            if cross_sum > plus_sum:
                local_max = cross_sum

            # 전체 최댓값 갱신
            if local_max > max_val:
                max_val = local_max

    print(f'#{tc} {max_val}')