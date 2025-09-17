from heapq import heappush, heappop

def prim(start_node):
    pq = [(0,start_node)] # (가중치, 노드)
    MST = [0] * (N+1) # visited처럼 사용
    min_weight = 0 # 최소 거리

    while pq:
        weight, node = heappop(pq) # 가장 작은 가중치

        # 이미 방문한 노드라면
        if MST[node]:
            continue

        # 아니라면
        MST[node] = 1 # node로 가는 최소 비용 선택
        min_weight += weight # 누적합 증가

        for next_node in range(N+1):
            # 갈 수 없으면 continue
            if graph[node][next_node] == 0:
                continue

            # 이미 방문했으면 continue
            if MST[next_node]:
                continue

            heappush(pq, (graph[node][next_node], next_node))

    return min_weight


# N(마지막 정점 번호), E(간선 개수)
N, E = map(int, input().split())

# 인접행렬 이용
graph = [[0] * (N+1) for _ in range(N+1)]
for _ in range(E):
    s, e, w = map(int, input().split())
    graph[s][e] = w # 단방향

# 프라임 알고리즘으로 풀어보기
result = prim(0)
print(f'#{result}')