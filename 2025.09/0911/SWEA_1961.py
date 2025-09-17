T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 90도 회전
    box_90d = [[0] * N for _ in range(N)]

    for r in range(N):
        for c in range(N):
            box_90d[c][N-1-r] = arr[r][c]

    # 180도 회전
    box_180d = [[0] * N for _ in range(N)]

    for r in range(N):
        for c in range(N):
            box_180d[N-r-1][N-c-1] = arr[r][c]


    # 270도 회전
    box_270d = [[0]* N for _ in range(N)]

    for r in range(N):
        for c in range(N):
            box_270d[N-c-1][r] = arr[r][c]

    print(f'#{tc}')
    for r90, r180, r270 in zip(box_90d, box_180d, box_270d):
        print(''.join(map(str, r90)),
              ''.join(map(str,r180)),
              ''.join(map(str,r270)))