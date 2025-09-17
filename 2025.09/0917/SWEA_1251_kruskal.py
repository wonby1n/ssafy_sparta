# 환경부담금 E * ((x1-x2)**2 + (y1-y2)**2)
# kruskal으로. 크루스칼은 간선 중심
# 그리고 union을 사용햇다?
def cal(i, j):
    return E * ((x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2)


def find_set(x):
    if x != p[x]:
        # 경로 압축 (대표자를 직접 저장)
        p[x] = find_set(p[x])
    return p[x]


def union(x, y):
    kx = find_set(x)
    ky = find_set(y)

    # 같은 집합이면 합칠 필요 없음
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
    # x, y 좌표가 따로 들어오므로
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    # 세율
    E = float(input())

    # 간선인가 만들어줘야됨
    edges = []
    for i in range(N):
        for j in range(i + 1, N):
            cost = cal(i, j)
            edges.append((cost, i, j))

    # 그다음에 정렬?햇는듯?
    edges.sort(key=lambda x: x[0])

    # 부모 만들어주기
    p = [i for i in range(N)]

    # 간선 수 셀 거
    cnt = 0
    # 원하는 답
    min_val = 0

    for val, x, y in edges:
        # 같은 집합이면은
        if union(x, y):
            cnt += 1
            min_val += val

        if cnt == N - 1:
            break

    print(f'#{tc} {round(min_val)}')
