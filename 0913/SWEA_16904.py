T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = []
    for _ in range(N):
        a, b = map(int, input().split())

        matrix.append((a,b))

    # 종료 시간 기준으로 정렬
    matrix.sort(key=lambda x: x[1])

    count = 0
    end_time = 0

    for s, e in matrix:  # (시작, 종료) 쌍을 s, e로 꺼냄
        if s >= end_time:  # 이전 작업 끝난 뒤 시작 가능하면
            count += 1
            end_time = e