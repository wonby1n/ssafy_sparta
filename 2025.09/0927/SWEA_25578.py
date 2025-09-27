T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    n_grid = [list(map(int, input().split())) for _ in range(N)]
    m_grid = [list(map(int, input().split())) for _ in range(M)]

    # 새 판넬 만들기
    cnt = N-M+1
    new_grid = [[0]* cnt for _ in range(cnt)]


    for r in range(N-M+1):
        for c in range(N-M+1):
            val = 0
            for k in range(M):
                for l in range(M):
                    val += n_grid[r+k][c+l]+m_grid[k][l]

            new_grid[r][c] = val

    print(f'#{tc}')
    for r in range(cnt):
        print(*new_grid[r])