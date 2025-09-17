T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    nbox = list(map(int, input().split()))
    mbox = list(map(int, input().split()))

    if N > M:
        N, M = M, N
        nbox, mbox = mbox, nbox

    max_val = 0

    # M은 N 숫자만큼 자기 인덱스를 다 돌아야 함

    for i in range(M-N+1):
        answer = 0
        for j in range(N):
            answer += mbox[i + j] * nbox[j]

        if max_val < answer:
            max_val = answer

    print(f'#{tc} {max_val}')