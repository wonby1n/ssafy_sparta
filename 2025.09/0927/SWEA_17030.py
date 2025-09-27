# 0번 지점에서 n번 지점까지 이동하는데 걸리는 최소한의 거리
# 모든 연결 지점을 거쳐가야 하는 거 아님 -> 다익스트라
# 다익스트라 -> 간선 리스트 만들어야 함

from heapq import heappop, heappush

def dijkstra(n):
    # 가중치, 노드 넣기
    heap = ([(0,n)])
    # 시작지점은 0이므로
    visited[n] = 0

    while heap:
        weight, node = heappop(heap)

        if visited[node] < weight:
            continue

        for next_w, next_n in grid[node]:
            new_w = next_w + weight

            if visited[next_n] > new_w:
                visited[next_n] = new_w

                heappush(heap, (new_w,next_n))

    return visited

T = int(input())
for tc in range(1, T+1):
    # 마지막 연결지점 번호 N, 도로의 개수 E
    N, E = map(int, input().split())
    N +=1
    grid = [[] for _ in range(N)]
    for _ in range(E):
        s, e, w = map(int, input().split())
        grid[s].append((w, e))

    INF = float('inf')
    visited = [INF] * (N+1)


    result = dijkstra(0)

    print(f'#{tc} {result[N-1]}')