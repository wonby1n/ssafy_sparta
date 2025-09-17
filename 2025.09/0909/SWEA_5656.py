# 벽돌깨기
# 1. 최소 벽돌
# - 현재 벽돌이 다 깨지면 더 이상 할 필요 없다 -> 현재 벽돌 수를 관리

# N번의 구슬을 굴려야 한다
# - 모든 케이스를 보아야 한다. (12^3, 약 25만번)
#   - 백트래킹
# - 한 번 쏘았을 때 벽돌들이 연쇄로 깨진다.
#   - 현재 기준으로 퍼져나가면서 탐색 (BFS)
#   - 빈칸 메우기

from collections import deque

def shoot(cnt, remains):
    global min_blocks
    # 종료 조건 : N개의 구슬을 모두 발사 or 남은 벽돌이 0이면
    if cnt == N or remains == 0:
        min_blocks = min(min_blocks, remains)
        return

    # 모든 열에 한 줄씩 떨구자
    for col in range(W):
        row = -1
        # 가장 위 벽돌을 검색
        for r in range(H):
            if arr[r][col]: # 벽돌이 있으면
                row = r
                break

        # 모든 열에 한 줄씩 떨구자
        for col in range(W):
            # 방법 1. 원본을 복사해두고, 다시 되돌리는 방법
            # 1. col 위치에 떨구기 전 상태를 복사 (얕은 복사 주의)
            # 2. 원본 리스트의 col 위치에 떨구고
            # 3. cnt + 1 번 재귀 상태로 이동
            # 4. 떨구기 전 상태로 복구

            # 방법 2. 복구 시간이 없는 방식

            copy_arr = [row[:] for row in now_arr]

            row = -1
            # 가장 위 벽돌을 검색
            for r in range(H):
                if copy_arr[r][col]: # 벽돌이 있으면
                    row = r
                    break

            if row == -1: # 벽돌이 없는 열은 pass
                continue

        # 해당 row, col의 숫자부터 시작해서 BFS
        # 행, 열, 숫자를 모두 담아야 한다
        q = deque([(row, col, arr[row][col])])
        now_remains = remains - 1
        arr[row][col] = 0 # 구슬이 처음 만나는 벽돌 자리

        # 주변 벽돌들을 순차적으로 파괴
        while q:
            r, c, p = q.popleft()
            for k in range(1, p):
                for i in range(4):
                    nr = r + (dy[i] * k)
                    nc = c + (dx[i] * k)

                    # 범위 밖이면 pass
                    if nr < 0 or nr >= H or nc < 0 or nc >= W:
                        continue

                    # 벽돌이 없으면 pass
                    if copy_arr[nr][nc] ==0:
                        continue

                    q.append((nr, nc, copy_arr[nr][nc])) # 다음 벽돌 추가
                    copy_arr[nr][nc] = 0 # 벽돌 깨짐
                    now_remains -= 1 # 숫자 감소소

        # 빈칸 메우기

        shoot(cnt+1, now_remains, copy_arr)


T = int(input())
for tc in range(1, T+1):
    N, W, H = map(int, input().split())
    arr = [list(map(int, input().split()))for _ in range(H)]
    min_blocks = 1e9 # 최소 벽돌 수
    blocks = 0
    # 남은 벽돌 수
    for i in range(H):
        for j in range(W):
            if arr[i][j]:
                blocks += 1


    shoot()
    print(f'#{tc} {min_blocks}')