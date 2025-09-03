
# txt 파일로 테스트할 때 하는 코드
# 제출할 때는 지워야 함
import sys
sys.stdin = open('input (1).txt', 'r')
# sys.stdout = open('output.txt', 'w')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 전체 위치에서 절대값 차이의 합
    total = 0

    # 델타배열 준비
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    for i in range(N):
        for j in range(N):
            # 현재 위치가 행번호 : i, 열번호 : j
            # 현재 위치에 있는 숫자 : num
            num = arr[i][j]

            abs_sum = 0

            # 상하좌우 요소 탐색하며 현재 위치에 있는 숫자의 차의 절댁값 구하기
            for d in range(4):
                # 이동 후 행 번호 (ni) = 현재 행 번호(i) + d 방향으로 이동했을때의 i의 변화량(di[d])
                ni = i + di[d]
                # 이동 후 열 번호 (nj) = 현재 열 번호(j) + d 방향으로 이동했을때의 j의 변화량(dj[d])
                nj = j + dj[d]

                # 주의할점 : 0,0에서 위로 이동하면 -1,0인데 이것은 유효한 위치(좌표)가 아님
                # 그래서 이동한 후에 인덱스(위치)가 유효한지 검사를 반드시 해야 한다.
                if 0 <= ni < N and 0 <= nj < N:
                    # 차 구하기 = (현재 위치에 있는 숫자 - ni,nj에 있는 숫자
                    sub = num - arr[ni][nj]
                    # 음수면 양수로 변환
                    if sub < 0:
                        sub = -sub

                    # 절대값 더하기
                    abs_sum += sub

            # 현재 위치 기준 델타탐색이 끝나면 i,j 위치 기준 차의 절댓값 합 구하기가 완료됨
            total += abs_sum

    print(f'#{tc} {total}')