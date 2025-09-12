n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# 1 *3 크기로 탐색

max_cnt = 0

for i in range(n):
    cnt = 0
    for j in range(n-2):
        max_cnt = max(max_cnt, grid[i][j] + grid[i][j+1] + grid[i][j+2])


print(max_cnt)