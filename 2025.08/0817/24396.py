T = int(input())
for _ in range(T):
    B, W, X, Y, Z = map(int, input().split())

    # 기본 점수 계산
    score = B * X + W * Y

    # 서로 다른 색에 넣을 때 이득
    another = (2 * Z) - (X + Y)

    if B < W:
        here = B
    else:
        here = W

    if another > 0:
        score += here * another

    print(score)