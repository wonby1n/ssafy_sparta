def recur(row, now_sum):
    global min_val
    # 종료조건 : 모든 행에 대해서 열 하나씩 선택하면
    if now_sum >= min_val:
        return

    if row == N:
        min_val = min(min_val, now_sum)
        return

    # 열 순회하기
    for col in range(N):
        # 만약 선택된 열이면
        if used[col]:
            continue
        used[col] = 1

        # 다음 행으로
        recur(row+1, now_sum + arr[row][col])

        used[col] = 0

T =int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 열 사용 여부를 체크한다
    used = [0] * N
    # 구하고 싶은 값
    min_val = float('inf')
    # 0번째 행부터 탐색
    recur(0,0)
    print(f'#{tc} {min_val}')