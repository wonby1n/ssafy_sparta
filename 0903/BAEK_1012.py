from collections import deque

T = int(input())
for tc in range(1, T+1):
    M, N, K = map(int, input().split())

    arr = [[0] * M for _ in range(N)]

    for _ in range(K):
        x, y = map(int, input().split())
        arr[y][x] = 1

    visited = [[0] * M for _ in range(N)]
    delta = [[-1,0],[1,0],[0,-1],[0,1]]
    cnt = 0

    for r in range(N):
        for c in range(M):
            if arr[r][c] == 1 and visited[r][c] == 0:
                q = deque()
                q.append([r, c])
                cnt += 1
                while q:
                    qr, qc = q.popleft()
                    visited[qr][qc] = 1
                    for dr, dc in delta:
                        nr = qr + dr
                        nc = qc + dc
                        if 0<=nr<N and 0<=nc<M and visited[nr][nc] == 0 and arr[nr][nc] == 1:
                            q.append([nr, nc])
                            visited[nr][nc] = 1

    print(cnt)