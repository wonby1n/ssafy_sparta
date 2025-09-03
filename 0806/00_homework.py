T = 10

for tc in range(1, T+10):
    input() # 첫번째 줄은 그냥 버리기
    # 100 x 100 배열 입력받기
    arr = [list(map(int, input().split())) for _ in range(100)]

    # 합을 구하면서, 동시에 최댓값 구하기
    # 원하는 최댓값 변수
    max_val = -float('inf') #python 정수 범위에서 가장 최솟값(무한대)

    # 1. 행의 합 구하기
    for r in range(100): # 행 우선순회
        # r이 고정된 상태에서
        sum = 0
        for c in range(100): # 열을 0부터 99까지 반복
            # (r, 0) ~ (r, 99)
            sum += arr[r][c]
            # sum <- r행의 합이 들어감
        if max_val < sum: # r행의 합과 max_val 비교
            max_val = sum # 업데이트

    # 2. 열의 합 구하기
    for c in range(100): # 열 우선순회
        # c가 고정된 상태에서
        sum =0
        for r in range(100): # 행 좌표를 반복
            # 고정 : [행좌표][열좌표]
            sum += arr[r][c]
        if max_val < sum:
            max_val = sum # 업데이트

    # 3. 대각선의 합 구하기
    # 우하향 대각선
    sum = 0
    for i in range(100):
        sum += arr[i][i]

    if max_val < sum:
        max_val = sum

    # 우상향 대각선
    # (r,c) r+c = 99
    # c = 99 - r
    sum = 0
    for i in range(100):
        sum += arr[i][99 - i]

    if max_val < sum:
        max_val = sum

    print(f'#{tc} {max_val}')