T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_val = 0

    for r in range(N):
        cnt = 0
        for c in range(N):
            # 1을 만났을 때는 1을 추가
            if arr[r][c] == 1:
                cnt += 1
            # 0을 만났을 때는
            else:
                if cnt == K:
                    max_val +=1
                cnt = 0

    for c in range(N):
        cnt = 0
        for r in range(N):
            if arr[r][c] == 1:
                cnt += 1
            # 0을 만났을 때는
            else:
                if cnt == K:
                    max_val +=1
                cnt = 0

    print(f'#{tc} {max_val}')