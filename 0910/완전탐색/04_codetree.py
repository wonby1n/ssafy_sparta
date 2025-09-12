n = int(input())
arr = list(map(int, input().split()))

min_val = float('inf')

# 모든 집(1~N)을 모임 장소로 가정
for m in range(1, n+1):
    total = 0
    # 각 집 i(1~N)에서 m까지 이동 거리
    for i in range(1, n+1):
        if i >= m:
            dist = i - m
        else:
            dist = m - i

        # 실제 인덱스는 0부터 시작하므로 1을 빼주고 이동 거리를 곱한다
        total += arr[i-1] * dist

    min_val = min(total,min_val)

print(min_val)