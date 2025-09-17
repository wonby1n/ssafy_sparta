# N개의 정수, 이웃한 M개의 합
N, M = int(input())
arr = list(map(int, input().split()))

# 구해야 하는 값의 초기값을 정해야 함
# 초기값은 arr[0]부터 M개까지 합을 더하는 것

result = 0
for i in range(M):
    result += arr[i]

# 초기값 세팅2
max_val = result
min_val = result

# 그다음에 반복문으로 1부터 M개를 더해야함
# N - M + 1 하는거는, 5-3+1 = 3 -> 2까지만 비교 (나머지는 인덱스 초과이므로)
# 5-2+1 = 4 -> 3까지만 비교
for i in range(1, N - M + 1):
    current_sum = 0 # 현재 구간의 합 초기화
    # 한 번에 i부터 M개만 비교해야 함
    for j in range(i, i + M):
        current_sum += arr[j]
    if max_val < current_sum:
        max_val = current_sum
    if min_val > current_sum:
        min_val = current_sum
