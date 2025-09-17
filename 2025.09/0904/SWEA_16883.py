# 우 하
delta = [[0,1],[1,0]]

# 현재위치 (i,j) i는 행번호, j는 열번호
# (0,0) -> 우 or 하 이동 반복 -> (N-1, N-1)
def solve(r, c):
    global min_sum, cnt
    # 종료
    if (r, c) == (N-1, N-1):
        # 도착했으니 합을 구하고
        # 그 합이 최소인가?
        if min_sum > cnt:
            min_sum = cnt
        return

    # 재귀호출 (다음단계)
    # 방향 선택지 2개 -> 재귀호출도 2개
    for dr, dc in delta:
        nr = r + dr
        nc = c + dc
        # 범위 안에 있으면
        if 0<=nr<N and 0<=nc<N:
            # 더해주고
            cnt += arr[nr][nc]
            solve(nr,nc)
            cnt -= arr[nr][nc]


T = int(input())
for tc in range(1, T + 1):
    # 가로세로 크기
    N = int(input())
    # 2차원 배열
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 문제에서 원하는 답 : 합이 최소가 되도록
    min_sum = 100000000
    # 알고 싶은 수 (시작점은 처음부터 더해준다)
    cnt = arr[0][0]

    solve(0,0)
    print(f'#{tc} {min_sum}')
