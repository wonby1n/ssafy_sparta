T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    grid = [list(map(int ,input().split())) for _ in range(N)]

    # 결과
    bug = 0

    # 큰 전체 안에서 파리채 시작 위치
    for r in range(N-M+1):
        for c in range(N-M+1):
            # 지금 잡은 파리의 수
            now_bug = 0
            # 파리채 안에서 작은 사각형만큼 탐색하기
            for k in range(M):
                for l in range(M):
                    # 탐색하려면 시작점에서 탐색거리만큼 더해줘야 함
                    now_bug += grid[r+k][c+l]

            bug = max(bug, now_bug)

    print(bug)