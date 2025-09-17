# 1. 집합 초기화
def make_set(n):
    parents = [i for i in range(n+1)]
    ranks = [0] * (n+1)
    return parents, ranks

# 2. 경로 압축
def find_set2(x):
    if x == parents[x]:
        return x
    parents[x] = find_set2(parents[x])  # 경로 압축
    return parents[x]

# 3. union (rank 기반)
def union(x, y):
    rep_x = find_set2(x)
    rep_y = find_set2(y)

    if rep_x == rep_y:
        return

    # rank가 낮은 쪽을 높은 쪽 밑으로
    if ranks[rep_x] < ranks[rep_y]:
        parents[rep_x] = rep_y
    elif ranks[rep_x] > ranks[rep_y]:
        parents[rep_y] = rep_x
    else:
        parents[rep_y] = rep_x
        ranks[rep_x] += 1


# 실행 예시
N = 6
parents, ranks = make_set(N)

union(2,4)
union(4,6)

if find_set2(2) == find_set2(6):
    print('2와 6은 같은 집합')
else:
    print('다른 집합')