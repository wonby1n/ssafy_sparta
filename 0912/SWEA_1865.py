def lets_work(row, lotto):
    global max_result
    if lotto*100 <= max_result:
        return

    # 모든 직원을 다 선택하면 종료
    if row == N:
        max_result = max(lotto*100, max_result)
        return

    # 순열
    for col in range(N):
        if used[col]:
            continue
        used[col] = 1

        lets_work(row+1, lotto*company[row][col])
        used[col] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    company = [list(map(lambda x: int(x)/100, input().split())) for _ in range(N)]
    print(company)

    max_result = 0
    used = [0] * N
    lets_work(0 ,1)

    print(max_result)