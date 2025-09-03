T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    answer = []

    if N <= M:

        for i in range(N):
            answer.append(a[i])
            answer.append(b[i])

        for j in range(N, M):
            answer.append(b[j])

    else:
        for i in range(M):
            answer.append(a[i])
            answer.append(b[i])

        for j in range(M, N):
            answer.append(a[j])

    print(f'#{tc}', *answer)