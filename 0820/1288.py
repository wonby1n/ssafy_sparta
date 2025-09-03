T = int(input())
for tc in range(1, T+1):
    N = int(input())

    # N의 배수 양을 셈
    # 셀때마다 나오는 숫자를 배열에 추가하기
    # 0에서 9까지 숫자 다 발견하면 그때 숫자 적기

    sheep = [0] * 10
    # 답
    answer = 0
    cnt = 0
    # 몇번 반복해야 될지 모르니까 while
    # sheep에 0이 사라질때까지
    while 0 in sheep:
        # n의 배수를 리스트로 저장한다
        cnt += 1
        idx = N * cnt
        for i in str(idx):
            # sheep i번에 1 추가
            sheep[(int(i))] = 1
        answer = idx

    print(f'# {tc} {answer}')