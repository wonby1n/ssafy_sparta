# prim은 heapq를 사용
from heapq import heappush, heappop

def prim(start_node):
    pq = [(0, start_node)] # (가중치, 노드)
    MST = [0] * (V+1)      # visited배열 만들기
    min_weight = 0

    while pq:
        weight, node = heappop(pq)

        # 가본적잇으면
        if MST[node]:
            continue

        # 아니라면 방문표시, 비용누적해주기
        MST[node] = 1
        min_weight += weight

        for next_node in range(V+1):
            # 갈 수 없으면 (0은 길이 없다는 뜻이니까)
            if graph[node][next_node] ==0:
                continue

            # 간 적 있으면
            if MST[next_node]:
                continue

            heappush(pq, (graph[node][next_node], next_node))

    return min_weight

T = int(input())
for tc in range(1, T+1):
    # V(마지막 노드번호) E(간선개수)
    V, E = map(int, input().split())

    # 인접 행렬로 저장하기
    graph = [[0] * (V+1) for _ in range(V+1)]
    for _ in range(E):
        s, e, w = map(int, input().split())
        graph[s][e] = w
        graph[e][s] = w # 양방향


    # 0번 방향부터 시작
    result = prim(0)
    print(f'#{tc} {result}')