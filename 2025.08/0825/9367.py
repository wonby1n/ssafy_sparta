T= int(input())
for tc in range(1, T+1):
    N = int(input())
    carrot = list(map(int, input().split()))

    answer = 1
    cnt = 1
    # 당근 다음꺼가 전보다 1 많으면
    for i in range(1, N):
        if carrot[i] > carrot[i-1]:
            cnt += 1
        else:
            cnt = 1

        if answer < cnt:
            answer = cnt

    print(f'#{tc} {answer}')