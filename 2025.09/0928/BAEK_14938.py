# 시간초과
from heapq import heappush, heappop

def dijkstra(start):
    heap = ([(0, start)])
    visited[start] = 0

    while heap:
        road, node = heappop(heap)

        if visited[node] < road:
            continue

        for next_r, next_n in graph[node]:
            new_r = next_r + road

            if visited[next_n] < new_r:
                visited[next_n] = new_r
                heappush(heap, (new_r, next_n))

    return visited

# 지역 개수, 수색범위, 길의 개수
N, M, R = map(int ,input().split())
# 아이템의 수
item_lst = [0] + list(map(int, input().split()))
graph = [[] for _ in range(N+1)]
for i in range(R):
    # 지역번호 a, b 길의 길이 l
    a, b, l = map(int, input().split())
    graph[a].append((l, b))

answer = 0
INF = float('inf')
visited = [INF] * (N + 1)

# 모든 정점을 시작점으로 다익스트라 실행
for i in range(1, N+1):
    dist = dijkstra(i)
    total = 0
    # 수색 범위 M 이하인 지역 아이템 합산
    for j in range(1, N+1):
        if dist[j] <= M:
            total += item_lst[j]
    answer = max(answer, total)

print(answer)