def cooking(row):
    if row == N:
        return




T = int(input())
for tc in range(1, T+1):
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]

    # 두 음식간의 맛의 차이가 최소가 되는 값
    result = 0

    used = [0] * N
    cooking(0)