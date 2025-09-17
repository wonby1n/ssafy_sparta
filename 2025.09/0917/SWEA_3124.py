# 크루스칼
def find_set(x):
    if x != p[x]:
        # 경로 압축 (대표자를 직접 저장)
        p[x] = find_set(p[x])
    return p[x]

def union(x, y):
    kx = find_set(x)
    ky = find_set(y)

    # 만약 대표자가 같으면 합칠 필요 없음
    if kx == ky:
        return False

    if kx < ky:
        p[ky] = kx
    else:
        p[kx] = ky
    return True


T = int(input())
for tc in range(1, T + 1):
    # V : 정점의 개수 E : 간선의 개수
    V, E = map(int, input().split())
    # 간선 정보 (A,B) 가중치 C
    graph = []
    for _ in range(E):
        # 노드, 가중치 순으로 들어옴
        a, b, c = map(int, input().split())
        graph.append((a, b, c))

    # 엄마아빠 만들기
    p = [i for i in range(V+1)]

    # 정렬하기(가중치로)
    graph.sort(key=lambda x: x[2])

    # 종료조건 들어갈 cnt
    cnt = 0
    # 원하는 값
    min_val = 0

    for next_r, next_c, cost in graph:
        if union(next_r, next_c):
            cnt += 1
            min_val += cost

        if cnt == V - 1:
            break

    print(f'#{tc} {min_val}')