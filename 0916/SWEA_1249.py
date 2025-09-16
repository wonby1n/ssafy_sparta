from heapq import heappop, heappush

dr = [-1,1,0,0]
dc = [0,0,-1,1]

def dijkstra(r,c):
    # (복구 시간, 출발점 r, c)
    heap = [(0,r,c)]
    # 출발 시간은 0
    times[r][c] = 0

    while heap:
        time, next_r, next_c = heappop(heap)

        if next_r == N-1 and next_c == N-1:
            return time

        for k in range(4):
            nr = next_r + dr[k]
            nc = next_c + dc[k]
            # 만약 범위 안이면
            if 0<=nr<N and 0<=nc<N:
                # 이것은 새로운 경로
                new_time = time + grid[nr][nc]

                # 새로운 경로가 더 짧으면
                if times[nr][nc] > new_time:
                    times[nr][nc] = new_time

                    heappush(heap, (new_time, nr,nc))

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    grid = [list(map(int, input().strip())) for _ in range(N)]

    # 무한대로 가정
    times = [[float('inf')] * N for _ in range(N)]
    # 출발은 0,0부터 한다고 했으므로
    result = dijkstra(0,0)
    print(f'#{tc} {result}')