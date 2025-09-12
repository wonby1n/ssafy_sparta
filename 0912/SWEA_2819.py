dy = [-1,1,0,0]
dx = [0,0,-1,1]

def recur(y, x, num):
    # 종료조건. 만약 7자리 다 이어붙였다면
    if len(num) == 7:
        answer.add(num)
        return

    # 재귀 호출? 쨌든 코드 적기
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        # 중복탐색 가능함. 범위는 벗어나면 안됨
        if 0<=ny<N and 0<=nx<N:
            # 다시 호출하고 문자 이어붙여줘야함
            recur(ny, nx, num + matrix[ny][nx])


T = int(input())
for tc in range(1, T+1):
    N = 4
    matrix = [input().split() for _ in range(N)]

    # 중복 가능
    # 서로 다른 7자리 수들의 개수 구하기
    answer = set()

    # 시작점
    for y in range(N):
        for x in range(N):
            recur(y, x, matrix[y][x])

    print(f'#{tc} {len(answer)}')