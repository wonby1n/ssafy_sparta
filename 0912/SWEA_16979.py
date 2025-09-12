# 순열
def recur(row, cost):
    global min_cost

    if cost >= min_cost:
        return
    # 종료조건. 3개 다 선택하면 종료
    if row == N:
        min_cost = min(min_cost, cost)
        return

    for col in range(N):
        if visited[col]:
            continue
        visited[col] = 1

        recur(row+1, cost+company[row][col])
        visited[col] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    company = [list(map(int, input().split())) for _ in range(N)]

    # 최소 생산 비용
    min_cost = 15 * 99
    # 열 사용 여부를 체크한다
    visited = [0] * N
    recur(0,0)
    print(f'#{tc} {min_cost}')
