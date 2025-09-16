from heapq import heappush, heappop

V, E = map(int, input().split())
g = [[] for _ in range(V)]
for i in range(E):
    s, e, w = map(int, input().split())
    g[s].append((e, w))
    g[e].append((s, w))


def prim(start):
    # 우선순위 큐(최소힙)
    heap = []
    # 중복체크배열
    # MST[i] = 1 : i번 정점은 MST에 포함 (이전에 골랐음)
    # MST[i] = 0 : i번 정점은 MST에 비포함 (이전에 고른적 없음)
    MST = [0] * V

    # 최소 비용
    min_w = 0

    # 정점을 선택한 횟수
    v_cnt = 0

    # 힙에 시작정점을 추가하고 반복 시작
    # (가중치, 정점번호) 형태로 힙에 추가, 이 때 힙의 우선순위 선정 기준은 튜플의 첫번째 원소, 시작점은 가중치 0
    heappush(heap, (0, start))

    # 선택한 정점의 개수가 V보다 작으면 아직 신장트리 완성 X
    # 큐안에 뭔가 남아 있어야 남아있는 가중치 중에 작은 거 선택
    while v_cnt < V and heap:
        # w : 가중치(힙안에서 최소였던)
        # v : 정점번호
        w, v = heappop(heap)

        # 내가 이전에 v번 정점을 선택한 적이 있다면
        if MST[v]:
            # 건너뜀
            continue

        # v가 이전에 선택한적 없는 정점 번호라면 MST에 추가
        MST[v] = 1
        # 가중치 합 누적
        min_w += w
        # 선택횟수 +1
        v_cnt += 1

        # v를 새로 MST에 추가했으니
        # v에서 새로 갈 수 있는 정점들의 정보도 heap에 추가
        for nv, nw in g[v]:
            # nv : v에서 갈 수 있는 정점 번호
            # nw : 그때의 가중치

            # nv 정점을 이전에 고른적 있으면 건너뛴다
            if MST[nv] == 1:
                continue

            # v -> nv로 가는 간선 정보 추가
            # 이 때 가중치는 nw
            heappush(heap, (nw, nv))


# 최소 신장트리의 가중치 합
print(f'최소 신장트리 가중치 합:{prim(0)}')
