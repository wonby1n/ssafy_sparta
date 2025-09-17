T = int(input())
for tc in range(1, T+1):
    N = int(input())

    graph = []

    # 총 합
    cnt = 0

    for _ in range(N):
        start, end = map(int, input().split())

        for now_start, now_end in graph:
            if start > now_start and end < now_end:
                cnt += 1
            elif start < now_start and end > now_end:
                cnt += 1

        graph.append((start, end))

    print(f'#{tc} {cnt}')