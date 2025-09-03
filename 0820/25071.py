T= int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    # 구하고 싶은 답
    step = 0
    # 현재 인덱스
    idx = 0
    # visited 배열
    visited = [0] * (N-1)
    while idx < N-1:
        # 만약 0번 인덱스이면
        if idx == 0:
            # 이동 횟수 1회 추가
            step += 1
            # 인덱스 1번으로 (다음 방으로)
            idx += 1
        # 만약 visited 배열이 1이면
        elif visited[idx] == 1:
            # 방문한 적 있으니 옆방으로 ㄱㄱ
            step += 1
            idx += 1
            # 만약 visited 배열이 0이면
        else:
            visited[idx] = 1
            step += 1
            idx = arr[idx] -1

    print(f'#{tc} {step}')