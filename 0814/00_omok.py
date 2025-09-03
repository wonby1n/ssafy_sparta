di = [0, 1, 1, 1]
dj = [1, 1, 0, -1]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [input() for _ in range(N)]

    # 답을 no라고 가정해놓고, 한 번이라도 yes면 끝
    ans = 'NO'
    for i in range(N): # 돌을 만나면
        for j in range(N):
            if arr[i][j] == 'o':
                for dir in range(4):  # 4방향 확인
                    cnt = 1  # i,j자리 돌부터 한 방향의 돌
                    for k in range(1, 5):  # 4개만 더 찾으면 yes
                        ni = i + di[dir] * k
                        nj = j + dj[dir] * k
                        if 0 <= ni < N and 0 <= nj < N and (arr[ni][nj] == 'o'):
                            cnt += 1
                            if cnt == 5:
                                ans = 'YES'
                        else:  # 판을 벗어나거나 돌이 아니면
                            break  # for k, 다음 방향으로 다시 조사
    print(f'#{tc} {ans}')