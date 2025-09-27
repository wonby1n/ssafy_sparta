n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

result = 0

for i in range(n):
    for j in range(n):
        for k in range(n):
            # 세 점 (i, j, k) 고르기
            if i == j or j == k or i == k:
                continue

            x1, y1 = points[i]
            x2, y2 = points[j]
            x3, y3 = points[k]

            if y1 == y2 and x1 == x3:
                base = abs(x1 - x2)   # 밑변 길이
                height = abs(y1 - y3) # 높이
                result = max(result, base * height)

print(result)
