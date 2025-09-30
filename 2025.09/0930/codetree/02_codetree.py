N, C, G, H = map(int, input().split())
ranges = [tuple(map(int, input().split())) for _ in range(N)]

# 후보 온도 모으기
candidates = set()
for a, b in ranges:
    candidates.add(a)
    candidates.add(b)
    candidates.add(a - 1)
    candidates.add(b + 1)

max_work = 0

# 각 후보 온도에서 작업량 계산
for T in candidates:
    total = 0
    for a, b in ranges:
        if T < a:
            total += C
        elif a <= T <= b:
            total += G
        else:  # T > b
            total += H
    max_work = max(max_work, total)

print(max_work)

