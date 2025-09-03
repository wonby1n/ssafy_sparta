T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 긴 거
    max_val = 0

    for r in range(N):
        cnt = 0
        for c in range(M):
            if arr[r][c] == 1:
                cnt += 1
                if max_val < cnt and cnt > 1:
                    max_val = cnt
            else:
                cnt = 0

    for c in range(M):
        cnt = 0
        for r in range(N):
            if arr[r][c] == 1:
                cnt += 1
                if max_val < cnt and cnt > 1:
                    max_val = cnt
            else:
                cnt = 0

    print(f'#{tc} {max_val}')