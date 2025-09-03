T = 10
for tc in range(1, T+1):
    int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    N = 100
    # 구하고 싶은 값 변수 정의
    max_val = 0

    # 행 열 대각선 순환하면 됨 제일 간단
    for r in range(N):
        first = 0
        for c in range(N):
            first += arr[r][c]
        if max_val < first:
            max_val = first

    for c in range(N):
        second = 0
        for r in range(N):
            second += arr[r][c]
        if max_val < second:
            max_val = second

    # 대각선 구하기
    third = 0
    for r in range(N):
        third += arr[r][r]
    if max_val < third:
        max_val = third

    fourth = 0
    for r in range(N):
        fourth += arr[r][N-1-r]
    if max_val < fourth:
        max_val = fourth

    print(f'#{tc} {max_val}')