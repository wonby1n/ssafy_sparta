T = int(input())  # 테스트 케이스 수 받고
for tc in range(1, T + 1):  # 테스트 케이스 돌면서
    N, M = map(int, input().split())  # N M 받아오고

    # 큰 정사각형을 만듦
    box = [list(map(int, input().split())) for _ in range(N)]

    # 총 죽은 파리 수
    max_dead = 0

    # 그냥 큰 정사각형 안에 작은 정사각형을 돌게 만들려면 이 4중 for문을 쓴다고 외우자
    # 이건 작은 정사각형이 큰 정사각형 안에서 도는 거
    for i in range(N - M + 1):
        for j in range(N - M + 1):

            # 지금 위치에서 알고 싶은 파리 수
            now_dead = 0

            # 이건 작은 정사각형 안에 있는 숫자들을 더해주는 거
           for k in range(M):
                for l in range(M):
                    # 현재 칸의 파리 수 더하기
                    now_dead += box[i+k][j+l]

            if max_dead < now_dead:
                max_dead = now_dead

    print(f'#{tc} {max_dead}')