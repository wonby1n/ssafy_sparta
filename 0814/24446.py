T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]


    delta = [[-1,0],[1,0],[0,-1],[0,1]]

    for r in range(N):
        for c in range(N):
            now = arr[r][c]
            min_val = arr[r][c]
            for dr, dc in delta:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < N and 0 <= nc < N:
                    if min_val > arr[nr][nc]:
                        min_val = arr[nr][nc]
            print(min_val)