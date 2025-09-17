# N 안에 M
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    big = [[0] * N for _ in range(N)]
    small = [[0] * M for _ in range(M)]

    gotohome = 1

    for r in range(N-M+1):
        for c in range(N-M+1):
            for i in range(M):
                for j in range(M):
                    big[r+i][c+j] = gotohome
            gotohome += 1
    print(f'#{tc}')
    for iwantmoney in big:
        print(*iwantmoney)