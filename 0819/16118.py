T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split())
    arr = list(map(int, input().split()))

    # 최대합
    max_val = 0

    for i in range(N):
        now_max = 0
        for j in range(i,i+M)
            now_max += arr[j]

        answer = max(max_val, now_max)

    print(f'#{tc} {answer}')