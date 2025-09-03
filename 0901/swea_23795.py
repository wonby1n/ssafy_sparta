T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 원하는 답
    answer = 0
    # 0 체크하기
    good = 0

    # 델타
    delta = [[-1,0],[1,0],[0,-1],[0,1]]

    # 시작점 구하기
    for r in range(N):
        for c in range(N):
            if arr[r][c] == 2:
                sr, sc = r, c
            if arr[r][c] == 0:
                good += 1


    for dr, dc in delta:
        for i in range(1, N):
            nr = sr + dr * i
            nc = sc + dc * i
            if 0 <= nr < N and 0 <= nc < N:
                if arr[nr][nc] == 1:
                    break
                if arr[nr][nc] == 0:
                    answer +=1 
            else:
                break
                

    print(f'#{tc} {good-answer}')