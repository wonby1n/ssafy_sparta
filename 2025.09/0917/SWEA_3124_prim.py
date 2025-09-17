# 프림은 정점기준, 우선순위큐 사용
from heapq import heappop, heappush


def prim(v):
    heap = [(0, v)]
    MST = [0] * (V + 1)
    min_val = 0

    while heap:
        cost, next_v = heappop(heap)

        # 만약 방문한 적이 있다면
        if MST[next_v]:
            continue

        MST[next_v] = 1
        min_val += cost

        for value, node in graph[next_v]:
            if MST[next_v]:


T = int(input())
for tc in range(1, T + 1):
    # V : 정점의 개수 E : 간선의 개수
    V, E = map(int, input().split())
    # 간선 정보 (A,B) 가중치 C
    graph = [[] for _ in range(V + 1)]
    for _ in range(E):
        # 노드, 가중치 순으로 들어옴
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        graph[b].append((a, c))
