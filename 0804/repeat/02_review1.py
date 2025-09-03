# N개의 정수, 이웃한 M개
# 배열 v
N, M = map(int, input().split())
V = list(map(int, input().split()))

# 초기 합: 첫 번째 구간 (0번 인덱스부터 M개)의 합을 미리 계산
count = 0
for i in range(M):
    count += V[i]

# 최대/최소 값을 처음 구간의 합으로 초기화
max_val = count
min_val = count

# N개에서 이웃한 M개를 비교하려면, 0개부터는 했으니
# 그 다음부터 N-M+1개까지만 비교하면 됨
# 왜 +1을 해주냐면, 5-3+1 = 3이니까. 2번 인덱스까지 갔을때 종료시켜야함
for i in range(1, N - M + 1):
    count_sum = 0
    # 한 번에 i부터 i+M개까지 합해야함
    for j in range(i, i + M):
        count_sum += V[j]
    if max_val < count_sum:
        max_val = count_sum
    if min_val > count_sum:
        min_val = count_sum

print(max_val - min_val)