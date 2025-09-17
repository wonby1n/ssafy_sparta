from collections import deque

def bfs(sr, sc):
    global answer
    q = deque()
    q.append((sr,sc))
    visited[sr][sc] = 1

    while q:
        # 안에 있는 좌표 꺼내고 비교하기
        qr, qc = q.popleft()
        # 종료조건
        if arr[qr][qc] == 3:
            visited[qr][qc] += 1
            return 1

        for dr, dc in [[-1,0],[1,0],[0,-1],[0,1]]:
            nr = qr + dr
            nc = qc + dc
            if 0<=nr<N and 0<=nc<N and visited[nr][nc] ==0 and arr[nr][nc] != 1:
                q.append((nr,nc))
                visited[nr][nc] = visited[qr][qc] + 1
    return 0


# 재귀호출
def dfs(sr, sc):
    global answer
    visited[sr][sc] = 1
    delta = [[-1,0],[1,0],[0,-1],[0,1]]
    if arr[sr][sc] == 3:
        answer = 1
        return
    else:
        for dr, dc in delta:
            nr = sr + dr
            nc = sc + dc
            if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0 and arr[nr][nc] != 1:
                dfs(nr, nc)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    visited = [[0] * N for _ in range(N)]
    answer = 0

    # 시작점 설정
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                sr, sc = i, j

    dfs(sr, sc)
    print(f'#{tc} {answer}')