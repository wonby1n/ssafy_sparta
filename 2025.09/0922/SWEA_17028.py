# 가중치를 모두 더해 출력 -> prim/kruskal
def find_set(x):
    if x != p[x]:
        p[x] = find_set(p[x])
    return p[x]

def union(x,y):
    kx = find_set(x)
    ky = find_set(y)

    if kx == ky:
        return False

    if kx < ky:
        p[ky] = kx
    else:
        p[kx] = ky

    return True


T = int(input())
for tc in range(1, T+1):
    # 마지막 노드번호 v, 간선개수 e
    V, E = map(int, input().split())
    graph = []
    for _ in range(E):
        s, e, w = map(int, input().split())
        graph.append((w,s,e))

    # 부모 만들기
    p = [i for i in range(V+1)]

    # 오름차순 정렬
    graph.sort()

    cnt = 0
    result = 0

    for w, x, y in graph:
        if union(x, y):
            cnt +=1
            result += w

        # 마지막 노드까지만 보기
        if cnt == V:
            break

    print(f'#{tc} {result}')