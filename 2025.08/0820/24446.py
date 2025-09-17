T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 일단 델타배열 쓰려나
    delta = [[-1,0],[1,0],[0,-1],[0,1]]

    # 구하고 싶은 답
    answer = 0

    for r in range(N):
        for c in range(N):
            # 현재 좌표
            now = arr[r][c]
            # 작은 거 구하기
            roll = 100
            for dc, dr in delta:
                nc = c + dc
                nr = r + dr
                if 0 <= nc < N and 0 <= nr < N:
                    min_val = arr[nc][nr]
                    if (min_val < now) and (roll > min_val):
                        roll = min_val

            print(roll)
