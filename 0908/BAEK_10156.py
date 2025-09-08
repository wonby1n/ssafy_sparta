K, N, M = map(int, input().split())

soda = K * N

if soda <= M:
    print(0)
elif soda > M:
    print(abs(M - soda))
