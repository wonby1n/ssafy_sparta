T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    delta = [[-1,0],[1,0],[0,-1],[0,1]]
    
    
    for r in range(N):
        for c in range(N):
            # 시작점 정하기
            sr, sc = r, c
            now = 1
            while True:
                wr, wc = sr, sc
                for dr, dc in delta:
                    for step in (1, N):
                        nr = sr + dr * step
                        nc = sc + dc * step
                        if 0<=nr<N and 0<=nc<N:
                            if arr[nr][nc] < min_val:
                                min_val = arr[nr][nc]
                                wr, wc = nr, nc
                    
                if wr == r and wc == r:
                    break

                r, c = wr, wc
                now += 1

print(now)