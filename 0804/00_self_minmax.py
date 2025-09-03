# N개의 정수, 이웃한 M개의 합
N, M = map(int, input().split())
# V 리스트
v = list(map(int, input().split()))

# 이웃한 M개의 합이 큰 경우와 작은 경우를 각각 구해야 함
# 그러기 위해서는 비교해야 하는 초기값을 설정
# max_val = 0, min_val = 0 으로 해도 되지만, 0부터 M번째까지 더한 값을 초기값으로 정해도 됨
# 그 값을 넣을 변수의 값을 0으로 설정
total = 0
# M개까지의 합을 반복문으로 구하고 total에 넣음
for i in range(M):
    total += v[i]

# total 값을 변수에 각각 넣어줌
max_val = total
min_val = total

# M개짜리 구간의 시작 인덱스를 1부터 순회
for i in range(1, N - M + 1):
    current = 0
    # 시작 i부터 M개 더하기
    for j in range(i, i+M):
        current += v[j]

    # 결과 더해줌
    if max_val < current:
        max_val = current
    if min_val > current:
        min_val = current

result = max_val - min_val
print(f'#{test_case} {result}')