# 크루스칼은 상호배타집합(유니온파인드)를 통해서 사이클의 유무 파악

# 대표 찾기
def find_set(x):
    if x == p[x]:
        return x

    # 경로압축
    p[x] = find_set(p[x])
    return p[x]


# x가 속한 집합과 y가 속한 집합을 합치는 연산
def union(x, y):
    kx = find_set(x)
    ky = find_set(y)

    # x와 y가 속한 집합의 대표가 같으면
    # 하나의 MST 안에 속해있는 거다
    # 이거를 또 추가해버리면 사이클이 생기게 된다
    if kx == ky:
        return

    if kx < ky:
        p[ky] = kx
    else:
        p[kx] = ky


# V : 정점의 개수
# E : 간선의 개수
V, E = map(int, input().split())

# 크루스칼은 간선정보만 리스트로 저장
edges = []

for i in range(E):
    # s, e : 정점번호
    # w : 가중치
    s, e, w = map(int, input().split())
    edges.append((s, e, w))

# 가중치는 튜플의 2번 인덱스니까 2번인덱스 원소를 기준으로 정렬
edges.sort(key=lambda x: x[2])

# make_set
p = [i for i in range(V)]

# 선택한 간선 수
cnt = 0
# 가중치 총합
result = 0

# 크루스칼 알고리즘은 인덱스 0번부터 차례대로 확인(정렬이 되어있음)
# 0번 인덱스에 있는 간선 => 가중치가 최소인 간선
for s, e, w in edges:
    # s, e 사이클 있는 간선의 가중치가 w인데
    # s, e가 한 집합에 속해있다면, 이 간선을 추가하면 사이클이 생긴다 => MST X
    # s, e가 한 집합에 속해있지 않다면 이 간선을 추가해도 사이클이 안생긴다. MST 0
    if find_set(s) != find_set(e):
        # s, e가 속한 집합을 합친다
        union(s, e)
        # 간선 개수 +1
        cnt += 1
        # 가중치 합
        result += w

        # 이 간선을 추가하고 내가 지금까지 선택한 간선 개수 == V-1이면 완성!

        if cnt == V - 1:
            break

print(result)