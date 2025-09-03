T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input()))

    # 구하고 싶은 값
    max_val = 0
    now = 0
    for i in range(N):
        if arr[i] == 1:
            now += 1
            if max_val < now:
                max_val = now
        else:
            now = 0

    print(f'#{tc} {max_val}')