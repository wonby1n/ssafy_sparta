from collections import deque

def bfs(r,c):
    q = deque()
    visited = [[0] * M for _ in range(N)]
    q.append((r,c))
    visited[r][c] = 1

    delta = [[-1,0],[1,0],[0,-1],[0,1]]

    while q:
        qr, qc = q.popleft()
        if qr == N-1 and qc == M-1:
            return visited[qr][qc]
        for dr, dc in delta:
            nr = qr + dr
            nc = qc + dc
            if 0<=nr<N and 0<=nc<M and visited[nr][nc] == 0 and maze[nr][nc] != 0:
                visited[nr][nc] =  visited[qr][qc] + 1
                q.append((nr,nc))



N, M = map(int,input().split())
maze = [list(map(int, input().strip())) for _ in range(N)]

s_r, s_c = 0,0

answer = bfs(s_r,s_c)
print(answer)