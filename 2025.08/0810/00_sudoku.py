# N = 9 M = 3
T = 10
for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]

    N, M = 9, 3
    sudoku = {1,2,3,4,5,6,7,8,9}
    first, second, third = 0, 0, 0
    # 사각형 안 사각형은 N-M+1 그러나 스도쿠는 중복 안해도 됨
    # 그럴려면 3개 검사하고 뛰어넘고 3개 검사하는 식으로 총 9번
    for r in range(0,N,M):
        for c in range(0,N,M):
            # arr[r][c] 하면 (0,0) (0,3) (0,6) ... 이렇게 출력됨
            start = []
            for i in range(M):
                for j in range(M):
                    start.append(arr[r+i][c+j])
            if set(start) == sudoku:
                first += 1

    # 행 시작
    for rr in range(N):
        start = []
        for cc in range(N):
            start.append(arr[rr][cc])
        if set(start) == sudoku:
            second += 1

    # 열 시장
    for cc in range(0, N):
        start = []
        for rr in range(N):
            start.append(arr[rr][cc])
        if set(start) == sudoku:
            third += 1

    if first+second+third == 27:
        print(1)
    else:
        print(0)