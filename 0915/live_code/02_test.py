N, M = map(int, input().split())


# 초기화
def make_set(n):
    parents = [i for i in range(n+1)]
    ranks = [0] * (n+1)
    return parents, ranks

# 부모 찾기
def find_set(x):
    if x != parents[x]:
        parents[x] = find_set(parents[x])
    return parents[x]

# 3. 합칠 때
def union(x,y):
    # 각자 부모를 찾음
    rep_x = find_set(x)
    rep_y = find_set(y)

    # 만약 부모가 같다면
    if rep_x == rep_y:
        return

    if ranks[rep_x] < ranks[rep_y]:
        # rep_x 트리 높이(rank)가 더 낮으면
        # rep_x를 rep_y 밑으로 붙임 (rep_y가 대표자 유지)
        parents[rep_x] = rep_y

    elif ranks[rep_x] > ranks[rep_y]:
        # rep_y 트리 높이가 더 낮으면
        # rep_y를 rep_x 밑으로 붙임 (rep_x가 대표자 유지)
        parents[rep_y] = rep_x
    else:
        # 두 트리 높이가 같으면
        # rep_y를 rep_x 밑으로 붙이고
        parents[rep_y] = rep_x
        # rep_x 트리 높이를 +1 해줌 (트리가 한 단계 더 깊어짐)
        ranks[rep_x] += 1


parents, ranks = make_set(N)