T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 구하고 싶은 값
    answer = 0

    for r in range(N):
        cnt = 0
        for c in range(N):
            # 만약 1을 만나면 cnt 1을 해준다
            if arr[r][c] == 1:
                cnt += 1
            # 만약 0을 만났을 때
            else:
                # cnt가 k와 같으면 답에 추가, 그리고 cnt 초기화
                if cnt == K:
                    answer +=1
                cnt = 0
        # 마지막까지 검사 후 cnt가 k와 같으면 정답에 1 추가
        if cnt == K:
            answer += 1

    for c in range(N):
        for r in range(N):
            cnt = 0
            # 만약 1을 만나면 cnt 1을 해준다
            if arr[r][c] == 1:
                cnt += 1
            # 만약 0을 만났을 때
            else:
                # cnt가 k와 같으면 답에 추가, 그리고 cnt 초기화
                if cnt == K:
                    answer += 1
                cnt = 0
        # 마지막까지 검사 후 cnt가 k와 같으면 정답에 1 추가
        if cnt == K:
            answer += 1

    print(f'#{tc} {answer}')