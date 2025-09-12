import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    H, W = map(int, input().split())
    matrix = [list(input()) for _ in range(H)]
    N = int(input())
    full_command = input()

    # 방향 (우,하,좌,상)
    dir_num = [0,1,2,3]

    for r in range(H):
        for c in range(W):
            if matrix[r][c] in '^v<>':
                sr, sc = r, c
    d1 = {'>': [0, 1], '<': [0, -1], '^': [-1, 0], 'v': [1, 0]}
    d2 = {'R': [0, 1], 'L': [0, -1], 'U': [-1, 0], 'D': [1, 0]}
    d3 = {'R': '>', 'L': '<', 'U': '^', 'D': 'v'}
    now_dir = d1[matrix[sr][sc]] # 지금 방향 [-1,0]

    power = max(H, W)

    # 입력받은대로 움직여야 됨
    for command in full_command:
        # 만약 쏘라고 하면 움직여야됨 (벽을 만날 때까지)
        # 길이는 H,W 둘 다 다르므로 둘 중 긴 거
        if command == 'S':
            for k in range(1, power):
                nr = sr + k * now_dir[0]
                nc = sc + k * now_dir[1]
                if 0<=nr<H and 0<=nc<W:
                    if matrix[nr][nc] == '*':
                        matrix[nr][nc] = '.'
                        break
                    elif matrix[nr][nc] == '#':
                        break
                    # 평지나 강을 만나면 계속한다
                    else:
                        continue

        # 만약 움직이라는 명령이면
        else:
            now_dir = d2[command]
            matrix[sr][sc] = d3[command]
            nr = sr + now_dir[0]
            nc = sc + now_dir[1]
            # 범위 안이고 평지라면 이동
            # 이동을 못해도 대가리는 바꿔야됨
            if 0<=nr<H and 0<=nc<W and matrix[nr][nc] =='.':
                    matrix[sr][sc] = '.'
                    sr, sc = nr, nc
                    matrix[sr][sc] = d3[command]

    print(f'#{tc}', end=' ')
    for i in matrix:
        print(''.join(map(str,i)))