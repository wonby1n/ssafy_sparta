# 10 x 10 격자에 빨간색(color1) 파란색(color2) 칠하기
# 2
# 2 2 4 4 1 [2,2] 부터 [4,4] 까지 color1 (빨강)
# 3 3 6 6 2 [3,3] 부터 [6,6] 까지 color2 (파랑)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    square = [[0] * 10 for _ in range(10)] # 10x10 격자 생성
    purple = 0

    # color 입력받기
    for _ in range(N):
        # c1, d1 = 왼쪽 위 좌표 / c2, d2 = 오른쪽 아래 좌표 / color = 색상(1=빨강, 2=파랑)
        c1, d1, c2, d2, color = map(int, input().split())
        # 해당 범위 안의 모든 칸을 순회하면서 색칠
        for i in range(c1, c2 + 1): # i는 행 번호
            for j in range(d1, d2 +1): # j는 열 번호

                # 빨간색이면 square에서 1을 더해준다
                if color == 1:
                    square[i][j] += 1
                # 파란색이면 2를 더해주기
                else:
                    square[i][j] += 2
    # 모든 칸을 순회하며 보라색(=값이 3인 칸) 개수 세기
    for i in range(10):
        for j in range(10):
            if square[i][j] == 3:
                purple += 1

    print(f'#{tc} {purple}')