from collections import deque

dr = [-1,1,0,0]
dc = [0,0,-1,1]

def bfs(r,c, num):
    # bfs 탐색 시작
    q = deque()
    q.append((r,c,num))

    while q:
        qr, qc, num = q.popleft()

        # 종료조건. 만약 num 길이가 7이라면
        # q에서 꺼냈을 때 검사해야 한다.
        if len(num) == 7:
            answer.add(num)
            continue

        for i in range(4):
            nr = qr + dr[i]
            nc = qc + dc[i]
            # 범위 안이라면
            if 0<=nr<N and 0<=nc<N:
                q.append((nr,nc,num+matrix[nr][nc]))

T = int(input())
for tc in range(1, T+1):
    N = 4
    matrix = [input().split() for _ in range(N)]

    # 중복 가능
    # 서로 다른 7자리 수들의 개수 구하기
    answer = set()

    for r in range(N):
        for c in range(N):
            bfs(r,c,matrix[r][c])

    print(f'#{tc} {len(answer)}')