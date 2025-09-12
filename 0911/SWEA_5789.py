T = int(input())
for tc in range(1, T+1):
    # N : 상자 수 Q : 실행 횟수
    N, Q = map(int, input().split())

    # box
    box = [0] * (N+1)
    for i in range(1, Q+1):
        # L번 상자부터 R번 상자까지 값을 i로 변경
        L, R = map(int, input().split())

        for j in range(L,R+1):
            box[j] = i

    box = box[1:]

    print(f'#{tc}', *box)