arr = [list(map(int, input().split())) for _ in range(4)]

result = 0

for r in range(4):
    for c in range(4):
        result += arr[r][c]