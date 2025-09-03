# N, 행 M, 열
T = int(input())
for tc in range(1, T+10):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 델타배열 사용하기

    # 일단 내가 구하고 싶은 max 변수 생성
    max_val = 0
    # 상하좌우 값 입력하기
    dr = [-1,1,0,0]
    dc = [0,0,-1,1]

    # 다중for문 시작
    # 행부터 순환
    for r in range(N):
        # 열도 순환
        for c in range(M):
            # 여기까지 하면, (0,1) (0,2) ... 이렇게 탐색 가능
            # 기준점이 되는 나를 지정
            balloon = arr[r][c]

            # 이제 내 상하좌우를 탐색 시작
            # 상하좌우는 늘 4번이므로 range 4를 입력
            for k in range(4):
                # 새로운 변수 넣기 시작
                nr = r + dr[k]
                nc = c + dc[k]
                if 0 <= nr < N and 0 <= nc < M:
                    balloon += arr[nr][nc]

            if max_val < balloon:
                max_val = balloon

    print(max_val)