T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))

    pos = 0

    # N 도착하기 전까지 반복
    while pos < N:
        # 리스트 끝부터 최대거리 가기
        for jump in range(K, 0, -1):

            # 만약 현재 위치가 도착점보다 낮고 1이라면
            if pos + jump < N and arr[pos + jump] == 1:
                # 현재 위치는 jump한 곳
                pos += jump
                break
        # 아니면 최대 위치만큼 도착하고 빠지자
        else:
            pos += K
            break

    if pos >= N - 1:  # 끝까지 갔거나 넘어간 경우
        pos = N
    else:
        pos += 1

    print(f'#{tc} {pos}')