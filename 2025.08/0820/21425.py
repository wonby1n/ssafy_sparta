T = int(input())
for tc in range(1, T+1):
    X, Y, N = map(int, input().split())

    cnt = 0

    # 몇 번 돌아야 될지 모르니 while
    # 답이 N보다 크게 된다면
    while X <= N and Y <= N:
        if X < Y:
            X += Y
            cnt += 1
        else:
            Y += X
            cnt += 1

    print(cnt)


"""
1 2 2
x += y
X = 1+2 X는 3, 초과
y += x
Y = 2+1 Y는 3, 초과

1 2 3
저장된 값이 3 초과되게
X += Y
X = 1+2 X는 3
X = 3+2 X는 5 -> 초과

Y += X
Y = 2+1 Y는 3
Y = 3+1 Y는 4 -> 초과

1 2 4
저장된 값이 4 초과되게
X += Y
X = 1+2 X는 3
X = 3+2 X는 5 -> 초과
Y += X
Y = 2+1 Y는 3
Y = 3+1 Y는 4
3번 해야 초과지만, X가 이미 초과이므로 2번
"""

