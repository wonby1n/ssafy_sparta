T = int(input())
for tc in range(1, T+1):
    N = int(input())
    room = list(map(int, input().split()))
    visited = [0] * N
    idx = 0
    cnt = 0
    while idx < N-1:
        if idx == 0:
            cnt += 1
            idx += 1
        elif 0 < idx < N-1:
            if visited[idx] == 0:
                cnt += 1
                visited[idx] = 1
                idx = room[idx] - 1
            else:
                cnt += 1
                idx += 1
        else:
            break

    print(f'#{tc} {cnt}')