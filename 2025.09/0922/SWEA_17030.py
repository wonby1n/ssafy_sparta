# 최소비용, 모든 연결 지점을 거치는 게 아니다 -> 다익스트라
from heapq import heappop, heappush

def dijkstra(node):
    heap = []
    # 가중치, 시작노드
    heap = [(0, node)]
    # 시작노드 최단거리는 0
    visited[node] = 0

    while heap:
        dist, node = heappop(heap)

        if visited[node] < dist:
            continue

        for next_d, next_n in graph[node]:
            new_d = next_d + dist

            # 새로운 거리가 더 작으면 갱신하기
            if visited[next_n] > new_d:
                visited[next_n] = new_d
                heappush(heap, (new_d, next_n))

    return visited


T = int(input())
for tc in range(1, T+1):
    # 마지막 연결지점 N, 도로의 개수 E
    N, E = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(E):
        s, e, w = map(int, input().split())
        graph[s].append((w,e))

    INF = float('inf')
    visited = [INF] * (N+1)

    # 0번 노드에서 실행
    result = dijkstra(0)
    print(f'#{tc} {result[N]}')