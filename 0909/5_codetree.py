OFFSET = 100  # -100을 보정하기 위한 값
SIZE = 201    # -100 ~ 100 => 총 201칸

n = int(input())
x1, y1, x2, y2 = [], [], [], []

# 입력 받기
for _ in range(n):
    a, b, c, d = map(int, input().split())
    x1.append(a + OFFSET)
    y1.append(b + OFFSET)
    x2.append(c + OFFSET)
    y2.append(d + OFFSET)

# 보정된 범위로 도화지 생성
grid = [[0] * SIZE for _ in range(SIZE)]

# 직사각형 덮기
for i in range(n):
    for x in range(x1[i], x2[i]):
        for y in range(y1[i], y2[i]):
            grid[x][y] = 1

# 넓이 계산
area = sum(sum(row) for row in grid)
print(area)
