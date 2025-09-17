# 크루스칼은 union 이용해서 하는거

# 대표자 찾기
def find_set(x):
    if x != p[x]:
        find_set(x)
    return p[x]

# 그룹 합치기
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


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    # x좌표 y좌표가 각각 따로 들어옴
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    # 환경부담금 세율
    E = float(input())

    # 크루스칼은 간선을 보는 알고리즘이기 때문에 간선을 만들어야 함
    edges = []
    for i in range(N):
        for j in range(i + 1, N):
            cost = E * ((x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2)
            edges.append((cost, i, j))

    # 1. 간선들 정렬하기
    edges.sort(key=lambda q: q[0])

    # 부모 찾아주기 (make-set)
    p = [i for i in range(N)]

    cnt = 0
    min_val = 0

    # 간선에서 정보 가져와서 하나씩 비교하기
    for value, x, y in edges:
        if union(x, y):
            cnt += 1
            min_val += value

        if cnt == N - 1:
            break

    print(f'#{tc} {round(min_val)}')