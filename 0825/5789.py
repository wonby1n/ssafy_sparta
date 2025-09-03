T = int(input())
for tc in range(1, T+1):
    N, Q = map(int, input().split())

    # 0인 상자 만들기
    box = [0] * N
    idx = 0

    # 입력되는 l과 r 받아주기
    for _ in range(1, Q+1):
        L, R = map(int,input().split())

        start = L - 1
        end = R
        idx += 1

        for i in range(start, end):
            box[i] = idx


    print(f'#{tc}', *box)