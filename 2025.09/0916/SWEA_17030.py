from heapq import heappop, heappush

def dijkstra(start):
    # 가중치, 시작노드
    hq = [(0, start)]
    D = [float('inf')] * V
    # 시작노드 최단거리는 0
    D[start] = 0
    while hq:
        nw, nv = heappop(hq)

        # 더 작은 값으로 드가있으면 버리자
        if D[nv] < nw:
            continue

        for next_node, next_weight in g[nv]:
            # 누적 거리 = 현재까지의 거리 + 다음 거리
            new_weight = nw + next_weight

            # 이미 작거나 같은 가중치로 온 적이 있다면 continue
            if D[next_node] <= new_weight:
                continue

            D[next_node] = new_weight
            heappush(hq, (new_weight, next_node))

    return D

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    V += 1
    g = [[] for _ in range(V)]
    # 인접행렬
    for _ in range(E):
        s, e, w = map(int, input().split())
        g[s].append((e,w))

    result = dijkstra(0)
    print(f'#{tc} {result[V-1]}')