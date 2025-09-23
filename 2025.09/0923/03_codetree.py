# 변수 선언 및 입력
n = int(input())
arr = list(map(int, input().split()))

cnt = 0
for i in range(n):  # 구간 시작
    for j in range(i, n):  # 구간 끝
        # 구간 합
        sum_interval = 0
        for k in range(i, j + 1):
            sum_interval += arr[k]

        # 평균
        avg = sum_interval / (j - i + 1)

        # 평균이 구간 안에 있으면 카운트
        for k in range(i, j + 1):
            if arr[k] == avg:
                cnt += 1
                break  # 이미 만족했으니 더 볼 필요 없음

print(cnt)
