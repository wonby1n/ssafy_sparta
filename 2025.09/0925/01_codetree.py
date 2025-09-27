n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

res = 40000*40000

# Please write your code here.
for i in range(len(points)):
    # i번째 점을 우선 제외하고,
    # 나머지 점들로 직사각형 넓이를 구한다.
    xs = []
    ys = []
    for j in range(len(points)):
        if i != j:
            x, y = points[j]
            xs.append(x)
            ys.append(y)

    min_x = min(xs)
    min_y = min(ys)
    max_x = max(xs)
    max_y = max(ys)

    area = (max_y - min_y) * (max_x - min_x)
    res = min(res, area)

print(res)
