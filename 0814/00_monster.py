def find_monster(N):
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                return i, j

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 0 빈칸 1 벽 2 괴물
    # si = sj = -1 # 괴물 위치 저장용 변수
    # for i in range(N):
    #     for j in range(N):
    #         if arr[i][j] == 2:
    #             si = i
    #             sj = j
    si, sj = find_monster(N)

    # 괴물이 상하좌우로 광선 발사
    for di, dj in [[-1,0],[1,0],[0,-1],[0,1]]:
        for k in range(1, N): # 레이저가 뻗어가는 거리
            ni, nj = si + di * k, sj + dj * k
            if 0 <= nj < N and 0 <= ni < N and (arr[ni][nj] == 0):
                arr[ni][nj] = 3       # 레이저가 지나감
            else:  # 공간을 벗어나거나 벽이면
                break   # for k, 다른 방향으로 발사
        # 안전한 칸 찾기
        ans = 0
        for i in range(N):
            for j in range(N):
                if arr[i][j] == 0:
                    ans += 1
    print(f'#{tc} {ans}')
