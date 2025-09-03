T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    # 얻고싶은 답
    step = 0
    # 현재 인덱스
    idx = 0
    # 방문 배열
    visited = [0] * (N-1)

    while idx < N-1:
        # while문을 계속 반복할 때 step에 1을 더해줌
        step += 1

        # 만약 0번 방이면 1번 방으로 이동한다
        if idx == 0:
            idx = 1

        # 만약 visited가 false면
        elif visited[idx] == 0:
            # 방문했다고 체크해주고
            visited[idx] = 1
            # 해당 idx에 적힌 방으로 이동한다 (0번방이 1번으로 붙여져있으므로 -1 해주기)
            idx = arr[idx] - 1
        # 만약 visited가 true면
        else:
            # 다음 방으로 이동한다
            idx += 1

    print(f'#{tc} {step}')