T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 몬스터의 위치를 구하자
    monster_r = 0
    monster_c = 0
    for r in range(N):
        for c in range(N):
            if arr[r][c] == 2:
                monster_r = r
                monster_c = c

    # 몬스터의 위치에서 광선을 쏘자
    for dr, dc in [[-1,0],[1,0],[0,-1],[0,1]]:
        for k in range(1, N):
            nr = monster_r + dr * k
            nc = monster_c + dc * k
            if 0 <= nr < N and 0 <= nc < N and (arr[nr][nc] == 0):
                arr[nr][nc] = 3
            else:
                break

    # 안전한 곳 찾기
    cnt = 0
    for r in range(N):
        for c in range(N):
            if arr[r][c] == 0:
                cnt += 1

    print(f'#{tc} {cnt}')