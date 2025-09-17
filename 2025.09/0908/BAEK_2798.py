N, M = map(int,input().split())
card = list(map(int, input().split()))

result = 0

# 3장의 합 비교하기
for i in range(N):
    for j in range(i+1, N):
        for c in range(j+1, N):
            sum_val = card[i] + card[j] + card[c]
            # 합이 M보다 작거나 같으면서, 기존 result보다 크면 result 갱신
            if (sum_val <= M) and (sum_val > result):
                result = sum_val

print(result)