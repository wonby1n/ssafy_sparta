# 최소비용 -> 다익스트라
from heapq import heappop, heappush

dr = [-1,1,0,0]
dc = [0,0,-1,1]

def dijkstra(r,c):
    heap = []
    # 가중치, 노드
    heap = [(0,r,c)]
    visited[r][c] = 0

    while heap:
        dist, node_r, node_c = heappop(heap)

        # 마지막 좌표에 도달하면 return
        if node_r == N-1 and node_c == N-1:
            return dist

        # 작으면 무시가능
        if visited[node_r][node_c] < dist:
            continue

        for k in range(4):
            nr = node_r + dr[k]
            nc = node_c + dc[k]
            # 범위 안이면
            if 0<=nr<N and 0<=nc<N:
                # 기본 이동 비용 추가
                cost = 1
                # 올라가면 높이 차이만큼 추가
                if grid[nr][nc] > grid[node_r][node_c]:
                    cost += grid[nr][nc] - grid[node_r][node_c]

                new_d = cost + dist

                if visited[nr][nc] > new_d:
                    visited[nr][nc] = new_d
                    heappush(heap, (new_d, nr,nc))

    return dist

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # 2차원 배열이 주어졌으므로 graph 따로 안 만들어도 됨
    grid = [list(map(int, input().split())) for _ in range(N)]

    INF = float('inf')
    visited = [[INF] * N for _ in range(N)]

    result = dijkstra(0,0)
    print(f'#{tc} {result}')