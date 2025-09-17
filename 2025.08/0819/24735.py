T = int(input())
for tc in range(1, T+1):
    N = int(input())
    box = list(map(int, input().split()))
    # 방의 세로 길이는 항상 100이다.
    # 즉, 상자는 최소 0, 최대 100 높이로 쌓을 수 있다
    # 밑에 있는 게 나랑 같거나 크면 낙차 -1

    # 구하고 싶은 낙차
    max_val = 0

    for i in range(N):
        # 낙차
        fall = 0
        for j in range(i, N):
            if box[i] > box[j]:
                fall += 1
            else:
                continue

        if max_val < fall:
            max_val = fall

    print(f'#{tc} {max_val}')