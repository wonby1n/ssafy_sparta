T = 10
for tc in range(1, 11):
    input() # 첫번째 줄의 tc 번호 무시
    arr = [list(map(int, input().split())) for _ in range(100)]

    #시작점 지정
    start_r, start_c = -1, -1
    # 출발점 찾기
    for r in range(100):
        for c in range(100):
            if arr[r][c] == 2:
                start_r, start_c = r,c

    r, c = start_r, start_c

    # 위로 올라가면서 경로 추적
    while r > 0:
        # 위로 올라가기 전에 좌우로 갈 수 있다면 먼저 좌우로 최대한 갈 수 있는 만큼 간다
        if c-1 > 0 and arr[r][c-1] == 1: # 왼쪽으로 갈 수 있다면
            while c - 1 >= 0 and arr[r][c-1] == 1:
                c -= 1
        elif c+1 < 100 and arr[r][c+1] == 1: # 오른쪽으로 갈 수 있다면
            while c+1 < 100 and arr[r][c+1] == 1:
                c += 1

        r -= 1 # 위로 이동

    print(f'#{tc} {c}')