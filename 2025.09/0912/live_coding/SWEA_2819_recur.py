dy = [-1,1,0,0]
dx = [0,0,-1,1]

# 1. 종료조건 : 숫자 7자리일 때 종료
# 2. 가지의 수 : 4개(상하좌우)
def recur(y, x, number):
    if len(number) == 7: # 7자리면 종료
        result.add(number) # set에 추가
        return

    for i in range(N): # 상하좌우
        ny = y + dy[i]
        nx = x + dx[i]

        # 범위 밖이면 다음 방향 확인 (continue)
        if ny < 0 or ny >= N or nx < 0 or nx >= N:
            continue

        # 다음 위치로 이동
        recur(ny, nx, number + matrix[ny][nx])


T = int(input())
for tc in range(1, T+1):
    N = 4
    matrix = [input().split() for _ in range(N)]
    result = set()

    # 7자리 만드는 코드
    # 4 X 4 가 모두 출발점이 될 수 있다
    for sy in range(N):
        for sx in range(N):
            recur(sy, sx, matrix[sy][sx])

    print(f'#{tc} {len(result)}')