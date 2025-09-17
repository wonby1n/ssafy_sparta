
# txt 파일로 테스트할 때 하는 코드
# 제출할 때는 지워야 함
import sys
sys.stdin = open('input (1).txt', 'r')
# sys.stdout = open('output.txt', 'w')


T = int(input())

for tc in range(1, T+1):
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]

    total = 0

    # ↘ 대각선
    for i in range(N):
        total += arr[i][i]

    # ↙ 대각선
    for i in range(N):
        total += arr[i][N-1-i]

    # N = 5라고 했으니 정중앙 겹치는 부분 존재
    total -= arr[N // 2][N // 2]

    print(f'#{tc} {total}')