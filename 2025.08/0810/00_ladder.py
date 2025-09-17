T = 10
for tc in range(1, 11):
    input()
    arr = [list(map(int, input().split())) for _ in range(100)]

    # 숫자가 들어와도 그냥 N으로 넣어주는게 덜 헷갈림
    N = 100

    # 끄트머리 좌표 (값 암거나 넣음)
    end_r, end_c = 0, 0

    # 맨 끝 좌표를 구해보자
    for r in range(N):
        for c in range(N):
            if arr[r][c] == 2:
                end_r, end_c = r, c

    # 여기서부터 시작
    # 이제 위로 올라가야함
    # 델타배열 (움직이는거) 적용시켜야 함
    # 상하좌우 델타
    # dr = [-1,1,0,0]
    # dc = [0,0,-1,1]
    # 근데 코드 쓰다보니까 참고만 하게 되고 안 썼네..

    # 올라가는 거니까 행이 0 되기 전까지 반복
    while end_r > 0:
        # 만약 왼쪽으로 갈 수 있는 상황이 되면
        if end_c - 1 > 0 and arr[end_r][end_c -1] == 1:
        # 왼쪽으로 갈 수 있을 때까지 가자
            while end_c - 1 > 0 and arr[end_r][end_c - 1] == 1:
                end_c -= 1

        # 만약 오른쪽으로 갈 수 있는 상황이 되면
        elif end_c + 1 < 100 and arr[end_r][end_c + 1] == 1:
            while end_c + 1 < 100 and arr[end_r][end_c + 1] == 1:
                end_c += 1

        # 둘 다 아니면 아니라니까 아니라느뇽 오라가짜
        end_r -= 1

    print(f'#{tc} {end_c}')