T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 행 열 돌기
    # 원하는 답
    answer = 0

    for r in range(N):
        cnt = 0
        for c in range(M):
            now = arr[r][c]

            if now == 1:
                cnt += 1
            else:
                cnt = 0

            if cnt > 1 and cnt > answer:
                answer = cnt

    for c in range(M):
        cnt = 0
        for r in range(N):
            now = arr[r][c]
            if now == 1:
                cnt += 1
            else:
                cnt = 0

            if cnt > 1 and cnt > answer:
                answer = cnt

    print(f'#{tc} {answer}')