def find_set(x):
    # 내가 대표자면 return
    if x == parents[x]:
        return x

    parents[x] = find_set(parents[x])
    return parents[x]

def union(x,y):
    kx = find_set(x)
    ky = find_set(y)

    if kx == ky:
        return

    if kx < ky:
        parents[ky] = kx
    else:
        parents[kx] = ky

T = int(input())
for tc in range(1, T+1):
    # V(마지막 노드번호) E(간선개수)
    V, E = map(int, input().split())
    graph = []
    # 인접리스트로 저장하기
    for _ in range(E):
        s, e, w = map(int, input().split())
        graph.append((s,e,w))

    # 1. 가중치 기준으로 오름차순 정렬
    graph.sort(key=lambda x:x[2])

    # 2. 서로소
    parents = [i for i in range(V+1)]

    # 정점 개수
    cnt = 0
    # 가중치 넣을거
    result = 0

    for u, v, w in graph:
        # 다르면 합쳐준다
        if find_set(u) != find_set(v):
            union(u, v)
            cnt += 1
            result += w

        # 마지막 노드 번호로 들어왔으므로, V까지만 보기
        if cnt == V:
            break

    print(f'#{tc} {result}')