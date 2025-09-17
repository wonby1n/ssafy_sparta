# 다익스트라는 우선순위큐 사용하는 거
# 최단 거리.
from heapq import heappop, heappush

dr = [-1,1,0,0]
dc = [0,0,-1,1]

def dijkstra(r,c):
    # 가중치, 출발지점
    heap = [(0,r,c)]
    # 출발지점 가중치는 0
    times[r][c] = 0

    while heap:
        # 이제부터 비교할 현재까지의 가중치, 노드
        time, next_r, next_c = heappop(heap)

        for k in range(4):
            nr = next_r + dr[k]
            nc = next_c + dc[k]
            # 범위 안이면 (다음꺼랑 비교하는 중. 그러니까 이제 새로운 값만들어야함)
            if 0<=nr<N and 0<=nc<N:
                new_time = time + times[nr][nc]

                # 새로운 경로가 더 짧으면 갱신
                if times[nr][nc] > new_time:
                    times[nr][nc] = new_time

    return times[N-1][N-1]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    grid = [list(map(int, input().strip())) for _ in range(N)]

    # 출발지는 언제나 (0,0) 도착지는 언제나 (N-1, N-1)
    dijkstra(0,0)

    INF = 21e9
    times = [[INF] * N for _ in range(N)]
