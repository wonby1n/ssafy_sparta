T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    v = list(map(int, input().split()))

    # 초기 최대합과 최소합은 0번째부터 M개 합으로 설정
    first_sum = 0
    for i in range(M):
        first_sum += v[i]

    max_sum = first_sum  # 최대값 초기화
    min_sum = first_sum  # 최소값 초기화

    # 1번째부터 M개 합을 구해야 함
    # 총 더하기 가능한 횟수는 N - M + 1개
    for i in range(1, N - M + 1):
        current_sum = 0  # 현재 구간의 합 초기화

        # 현재 위치 i부터 M개의 값을 더함
        for j in range(i, i + M):
            current_sum += v[j]

        # 최대값과 최소값 비교 후 갱신
        if max_sum < current_sum:
            max_sum = current_sum
        if min_sum > current_sum:
            min_sum = current_sum

    # 최종 정답: 최대합 - 최소합
    result = max_sum - min_sum

    # 형식에 맞게 출력
    print(f"#{test_case} {result}")