T = int(input())
for tc in range(1, T+1):
    D, A, B, F = map(int, input().split())

    train = D / (A + B)

    fly = F * train
    print(fly)