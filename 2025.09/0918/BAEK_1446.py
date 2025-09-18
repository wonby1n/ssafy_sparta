# 크루스칼 하니까 답이 안나옴

def find_set(x):
    if x != p[x]:
        p[x] = find_set(p[x])
    return p[x]


def union(x, y):
    kx = find_set(x)
    ky = find_set(y)

    if kx == ky:
        return False

    if kx < ky:
        p[ky] = kx
    else:
        p[kx] = ky
    return True


N, D = map(int, input().split())
# 그래프 필요함
edges = []
for _ in range(N):
    s, e, w = map(int, input().split())
    edges.append((s, e, w))

p = [i for i in range(10001)]

# 정렬
edges.sort(key=lambda x: x[2])

cnt = 0
result = 0

for s, e, w in edges:
    if union(s, e):
        cnt += 1
        result += w

    if cnt == N - 1:
        break

print(result)