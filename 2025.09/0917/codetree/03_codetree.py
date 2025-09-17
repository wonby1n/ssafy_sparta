dys = [1, 0, -1, 0]
dxs = [0, 1, 0, -1]

n = int(input())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

def in_range(r, c):
    return 0 <= r < n and 0 <= c < n

def count_one(r, c):
    cnt = 0

    # (r, c)를 중심으로 할 때,
    # 상하좌우에 1이 몇개 있는지
    for i in range(4):
        nr = r + dys[i]
        nc = c + dxs[i]

        if not in_range(nr, nc):
            continue

        if grid[nr][nc] == 1:
            cnt += 1

    return cnt

res = 0
for r in range(n):
    for c in range(n):
        cnt = count_one(r, c)
        if cnt >= 3:
            res += 1

print(res)