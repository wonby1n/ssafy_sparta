dr = [-1,1,0,0]
dc = [0,0,-1,1]

def recur(sr,sc, num):
    # 종료조건. 만약 이어붙인 숫자가 7자리가 되면,
    if len(num) == 7:
        result.add(num)
        return

    for k in range(4):
        nr = sr + dr[k]
        nc = sc + dc[k]
        if 0<=nr<N and 0<=nc<N:
            recur(nr,nc,num + matrix[nr][nc])


T = int(input())
for tc in range(1, T+1):
    N = 4
    matrix = [list(input().split()) for _ in range(N)]
    result = set()
    # 시작점 정하기
    for r in range(N):
        for c in range(N):
            recur(r,c, matrix[r][c])

    print(len(result))