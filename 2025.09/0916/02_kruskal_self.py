# 크루스칼은 union 이용해서 하는 거
def find_set(x):
    # 만약 자기 자신이 루트라면 반환
    if x == parents[x]:
        return x

    # 경로 압축 : 재귀로 자기의 부모를 찾으면서 갱신
    parents[x] = find_set(parents[x])
    return parents[x]

def union(x, y):
    kx = find_set(x)
    ky = find_set(y)

    if kx == ky:
        return

    # 작은 번호를 루트로
    if kx < ky:
        parents[ky] = kx
    else:
        parents[kx] = ky


# 정점 개수, 간선 개수
V, E = map(int, input().split())

# 인접리스트 이용
edges = []
for _ in range(E):
    s, e, w = map(int, input().split())
    edges.append((s,e,w)) # 간선들의 정보를 저장

# 1. 가중치 기준으로 오름차순 정렬
edges.sort(key=lambda x:x[2])

# 2. union find 코드 시작

# make-set (처음에는 자기 자신이 부모)
parents = [i for i in range(V)]

# 선택한 간선 수
cnt = 0
# 가중치 총합
result = 0

# 3. 간선 하나씩 선택
for u,v,w in edges:
    if find_set(u) != find_set(v): # 부모가 다르면
        union(u, v) # 합쳐추고
        cnt += 1    # 간선 선택해주고
        result += w # 비용 누적해주고

        if cnt == V-1:
            break

print(result)