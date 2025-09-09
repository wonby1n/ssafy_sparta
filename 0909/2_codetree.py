n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# 상하좌우
del_r = [-1, 1, 0, 0]
del_c = [0, 0, -1, 1]

answer = 0

for r in range(n):
    for c in range(n):
        cnt = 0
        for dr, dc in zip(del_r, del_c):
            nr = r + dr
            nc = c + dc
            if 0 <= nr < n and 0 <= nc < n:
                if grid[nr][nc] == 1:
                    cnt += 1

        if cnt >= 3:
            answer += 1

print(answer)