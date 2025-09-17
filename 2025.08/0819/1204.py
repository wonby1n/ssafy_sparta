T = int(input())
for tc in range(1, T+1):
    t = int(input())
    arr = list(map(int, input().split()))
    N = len(arr)

    # 원하는 값
    max_score = 0
    max_idx = 0

    score = [0] * 101

    for i in range(N):
        score += arr[i]

    for i in range(101):
        # 같은 빈도면 높은 점수를 저장해야 하므로 >= 비교
        if score[i] >= max_score:
            max_score = score[i]
            max_idx = i

    print(f'#{tc} {max_idx}')