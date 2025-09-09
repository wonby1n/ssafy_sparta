N, K = map(int, input().split())
count = [0] * (N + 1)   # 1번부터 N번까지 사용

for _ in range(K):
    a, b = map(int, input().split())
    for i in range(a, b + 1):   # 범위 직접 증가
        count[i] += 1

# 최댓값 찾기
max_blocks = 0
for x in count[1:]:  # 1번 칸부터 N번 칸까지
    if x > max_blocks:
        max_blocks = x

print(max_blocks)
