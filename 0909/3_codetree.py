n = int(input())
moves = [tuple(input().split()) for _ in range(n)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]

s_r, s_c = 0, 0

# 상 하 좌 우
delta = [[1,0],[-1,0],[0,-1],[0,1]]

for i in range(n):
    # 북쪽(상)
    if dir[i] == 'N':
        s_r = s_r + delta[0][0] * dist[i]
    # 남쪽(하)
    elif dir[i] == 'S':
        s_r = s_r + delta[1][0] * dist[i]
    # 서쪽(좌)
    elif dir[i] == 'W':
        s_c = s_c + delta[2][1] * dist[i]
    # 동쪽(우)
    elif dir[i] == 'E':
        s_c = s_c + delta[3][1] * dist[i]

print(s_c,s_r)