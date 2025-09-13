# 숫자는 1부터 N^2이하로, 다 다르게 적혀 있다
# 현재 방에 적힌 숫자보다 1 커야지 상하좌우로 이동 가능
# 가장 많은 개수의 방을 이동해야 함
# DFS로 풀어보자. 근데 DP가 정석이겠지?
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def my_style(sr, sc):
    # 만약 간 적이 있다면
    if dp[sr][sc] != 0:
        return dp[sr][sc]

    dp[sr][sc] = 1

    for k in range(4):
        nr = sr + dr[k]
        nc = sc + dc[k]
        if 0<=nr<N and 0<=nc<N and matrix[sr][sc]+1 == matrix[nr][nc]:
            dp[sr][sc] = max(dp[sr][sc], 1 + my_style(nr,nc))

    return dp[sr][sc]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    # 처음에 출발해야 하는 방 번호와 최대 몇 개의 방을 이동할 수 있는지
    # dp로 한 번 풀어보자...
    # dp는 시작점에 몇 개의 방을 이동할 수 있는지 적혀있으니까
    # 2차원 배열로 만들어주기
    dp = [[0] * N for _ in range(N)]

    # 원하는 값
    max_len = 0
    start_num = N*N+1

    for r in range(N):
        for c in range(N):
            length = my_style(r, c)

            # 더 긴 경로 찾으면 갱신
            if length > max_len:
                max_len = length
                start_num = matrix[r][c]

            # 길이가 같으면 더 작은 시작 숫자 선택
            elif length == max_len and matrix[r][c] < start_num:
                start_num = matrix[r][c]