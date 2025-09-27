# 최적의 경로로 이동, 최소한의 연료
# 다익스트라
from heapq import heappop, heappush

drs = [-1,1,0,0]
dcs = [0,0,-1,1]

def dijkstra(r,c):
    heap = ([(0, r, c)])
    visited[r][c] = 0

    while heap:
        weight, node_r, node_c = heappop(heap)

        if visited[node_r][node_c] < weight:
            continue

        if node_r == N-1 and node_c == N-1:
            return weight

        for dr, dc in zip(drs,dcs):
            nr = dr + node_r
            nc = dc + node_c
            if (0<=nr<N and 0<=nc<N):
                cost =1
                if grid[node_r][node_c] < grid[nr][nc]:
                    cost += grid[nr][nc]-grid[node_r][node_c]

                new_c = cost + weight

                if visited[nr][nc] > new_c:
                    visited[nr][nc] = new_c
                    heappush(heap, (new_c,nr,nc))

    return weight


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    grid = [list(map(int, input().split()))for _ in range(N)]

    INF = float('inf')
    visited = [[INF] * N for _ in range(N)]

    dijkstra(0,0)