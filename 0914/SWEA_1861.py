dr = [-1,1,0,0]
dc = [0,0,-1,1]

def dfs(sr,sc):
    # 종료조건. 이미 가본적 있으면
    if dp[sr][sc] != 0:
        return dp[sr][sc]

    # dp 호출
    dp[sr][sc] = 1
    for k in range(4):
        nr = sr + dr[k]
        nc = sc + dc[k]
        if 0<=nr<N and 0<=nc<N and matrix[nr][nc] == matrix[sr][sc] +1:
            dp[sr][sc] = max(dp[sr][sc], 1+dfs(nr,nc))

    return dp[sr][sc]

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]

# 원하는 값 : 가장 많은 개수의 방을 이동할 수 있는 곳
# 출발하는 곳, 이동 몇번하는지
result = 0
start_num = -1
# dp 배열
dp = [[0] * N for _ in range(N)]

# 출발점
for r in range(N):
    for c in range(N):
        lenth = dfs(r,c)

        # 길면 갱신
        if lenth > result:
            result = lenth
            start_num = matrix[r][c]

        # 같은 길이 나오면 시작점이 더 작은 걸로
        elif lenth == result:
            if matrix[r][c] < start_num:
                start_num = matrix[r][c]

print(f'#{start_num} {result}')