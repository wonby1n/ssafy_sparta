from heapq import heappush, heappop

def dijkstra(v):
    # 가중치, 노드
    heap = [(0,v)]
    # 시작노드 거리는 0
    INF = float('inf')
    MST = [INF] * (D + 1)
    MST[v] = 0

    while heap:
        weight, node = heappop(heap)

        # 방문했으면 무시
        if MST[node] < weight:
            continue

        for next_w, next_n in graph[node]:
            new_w = weight + next_w

            # 이미 작은게 있으면 무시하고 continue
            if MST[next_n] <= new_w:
                continue

            MST[next_n] = new_w
            heappush(heap, (new_w, next_n))

    return MST

N, D = map(int, input().split())

graph = [[] for _ in range(D+1)]
for _ in range(N):
    s, e, w = map(int, input().split())
    graph[s].append((w, e))


# 0번 노드부터 시작
result = dijkstra(0)
print(result)