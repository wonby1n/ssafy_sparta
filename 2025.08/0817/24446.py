T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 가장 많이 이동한 거리 저장
    max_move = 0

    for r in range(N):
        for c in range(N):
            # 시작 위치 저장
            sr = r
            sc = c
            cnt = 1  # 자기 자신 포함해서 1칸부터 시작
            # 이동 시작
            while True:
                now_val = arr[sr][sc]
                # 다음 이동할 후보 칸 초기화
                next_r = -1
                next_c = -1
                min_val = 100  # 문제 조건상 최대 숫자는 99이므로

                # 상하좌우
                for dr, dc in [[-1,0],[1,0],[0,-1],[0,1]]:
                    nr = sr + dr
                    nc = sc + dc
                    if 0 <= nr < N and 0 <= nc < N:
                        # 지금보다 작을 때
                        if arr[nr][nc] < now_val:
                            # 갱신되어 있는 값보다 더 작은 값이면 갱신
                            if arr[nr][nc] < min_val:
                                min_val = arr[nr][nc]
                                next_r = nr
                                next_c = nc

                # 이동할 칸이 없다면 종료
                if next_r == -1 and next_c == -1:
                    break

                # 다음 위치로 이동
                sr = next_r
                sc = next_c
                cnt += 1  # 한 칸 이동했으므로 +1

            # 최대 이동 거리 갱신
            if cnt > max_move:
                max_move = cnt

    # 출력
    print(f'#{tc} {max_move}')