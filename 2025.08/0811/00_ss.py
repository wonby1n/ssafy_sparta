T = 10
for tc in range(1, T+1):
    arr = [list(input()) for _ in range(100)]
    N = len(arr)

    # 결과를 위한 변수 만들기
    result = 0

    # 반복문 시작
    for r in range(N):
        for c in range(N-M+1):
            # 안에서 반복 가능, 이제 뭘 해야 되지?
            # 안에서 반복했을 때... 회문인 걸 찾아야 함. 길이는 상관 x
            # 제일 긴 회문의 길이를 출력해야 함
            for k in range()