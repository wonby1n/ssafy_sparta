# 델타 상하좌우 배열
dr = [-1,1,0,0]
dc = [0,0,-1,1]

def panda_moving(sr, sc, move):
    global max_val
    # 가지치기
    # 현재까지 길이를 최댓값과 비교
    max_val = max(move, max_val)

    # 델타로 이동하기
    for k in range(4):
        nr = sr + dr[k]
        nc = sc + dc[k]
        # 만약 범위 안에 있고 현재 좌표보다 대나무가 많으면
        if 0<=nr<N and 0<=nc<N and matrix[nr][nc] > matrix[sr][sc]:
            # 판다는 먹으러 간다
            panda_moving(nr, nc, move+1)


N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]

# 원하는 답
max_val = 0

# 시작점 정해주는 동시에 함수 호출
for r in range(N):
    for c in range(N):
        panda_moving(r, c, 1)

print(max_val)