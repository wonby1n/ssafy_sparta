# 순서 상관 없음 -> K개중에 N개
# 조합
# 델타배열
dr = [-1,1,0,0]
dc = [0,0,-1,1]

def recur(sr,sc,num):
    # 종료조건. 만약 7개 다 셋다면, 종료시키기
    if len(num) == 7:
        seven_words.add(num)
        return

    for k in range(4):
        nr = sr + dr[k]
        nc = sc + dc[k]
        # 범위 안에 있으면 continue
        if 0<=nr<N and 0<=nc<N:
            recur(nr,nc, num + matrix[nr][nc])


T = int(input())
for tc in range(1, T+1):
    N = 4
    matrix = [list(input().split()) for _ in range(N)]
    # 델타배열로 돌아다니며 만들어야 할 단어의 길이가 7개
    # 만든 단어는 중복 X
    # 간 곳 또 가도 됨
    # 원하는 값. 서로 다른 일곱 자리 수들의 개수
    seven_words = set()

    # 시작점 결정
    for r in range(N):
        for c in range(N):
            recur(r, c, matrix[r][c])

    print(len(seven_words))