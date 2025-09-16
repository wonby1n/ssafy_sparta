from heapq import heappop, heappush

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def dijkstra(sr, sc):
    # 가중치, 출발 노드 정하기..
    hq = [(0, sr, sc)]
    D = [[float('inf')] * N for _ in range(N)]
    # 출발점은 cost가 0이므로
    D[sr][sc] = 0

    while hq:
        # 가중치, (좌표 r, c)
        dist, node_r, node_c = heappop(hq)

        # 마지막에 도착하면 return
        if node_r == N - 1 and node_c == N - 1:
            return dist

        for k in range(4):
            nr = node_r + dr[k]
            nc = node_c + dc[k]
            # 범위 안이면
            if 0 <= nr < N and 0 <= nc < N:
                # 기본 이동 비용 추가
                cost = 1
                # 올라가면 -> 높이 차이만큼 추가
                if grid[nr][nc] > grid[node_r][node_c]:
                    cost += grid[nr][nc] - grid[node_r][node_c]

                new_dist = dist + cost

                # 좌표에 있는게 새로 계산한 값보다 작으면 지나가기
                if D[nr][nc] <= new_dist:
                    continue

                # 작으면 좌표에 있는 값 갱신해주기
                D[nr][nc] = new_dist
                heappush(hq, (new_dist, nr, nc))
    # 루프 다 돌고
    return dist

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]

    # 출발은 매번 맨 왼쪽 위
    result = dijkstra(0, 0)
    print(f'#{tc} {result}')