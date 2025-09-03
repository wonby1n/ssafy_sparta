T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]

    # 정답 아니라고 가정
    answer = 'NO'

    # 델타 상하좌우 대각선
    delta1 = [[-1,0],[1,0],[0,-1],[0,1]]
    delta2 = [[-1,-1],[-1,1],[1,-1],[1,1]]

    for r in range(N):
        for c in range(N):
            if arr[r][c] == 'o':
                for dr, dc in delta1:
                    cnt = 1
                    for k in range(1, 5):
                        nr = r + dr * k
                        nc = c + dc * k
                        if 0 <= nr < N and 0 <= nc < N and (arr[nr][nc] == 'o'):
                            cnt += 1
                            if cnt >= 5:
                                answer = 'YES'
                        else:
                            break
                for dr, dc in delta2:
                    cnt = 1
                    for k in range(1, 5):
                        nr = r + dr * k
                        nc = c + dc * k
                        if 0 <= nr < N and 0 <= nc < N and (arr[nr][nc] == 'o'):
                            cnt += 1
                            if cnt >= 5:
                                answer = 'YES'
                        else:
                            break

    print(f'#{tc} {answer}')