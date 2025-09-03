T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().strip())) for _ in range(N)]

    # 반갈죽 하기
    half = N // 2
    answer = 0

    # 각 행마다 차지하는 구간 계산하기
    for r in range(N):
        # 중앙과의 거리
        d = abs(half - r)
        # 시작 열
        start = d
        # 끝 열
        end = (N-1)-d
        for c in range(start, end +1):
            answer += arr[r][c]