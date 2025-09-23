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
    N, M = map(int, input().split())
    # 부모 만들기
    p = [i for i in range(N+1)]
    # 입력받으면서 각자 합치기
    for _ in range(M):
        a, b = map(int, input().split())
        union(a,b)

    # 대표자 몇 명인지 세기
    result = set()

    for i in range(1, N+1):
        result.add(find_set(i))

    print(f'#{tc} {len(result)}')