n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

max_cnt = 0

# 1*3 으로 탐색하면서 숫자 1을 세라

# 격자 탐색 시작 (행)
for r in range(n):
    # (열)
    for c in range(n-2):
        max_cnt = max(max_cnt, grid[r][c]+grid[r][c+1]+grid[r][c+2])

print(max_cnt)
