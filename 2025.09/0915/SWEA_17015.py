'''
예를 들어 1번-2번, 1번-3번이 같은 조가 되고 싶다고 하면, 1-2-3번이 같은 조가 된다.
번호를 적지도 않고 다른 사람에게 지목되지도 않은 사람은 단독으로 조를 구성하게 된다.

1번부터 N번까지의 출석번호가 있고,
M 장의 신청서가 제출되었을 때, 전체 몇 개의 조가 만들어지는지 출력
5 2
1 2 3 4
'''


# 초기화
def make_set(n):
    parents = [i for i in range(n + 1)]
    ranks = [0] * (n + 1)
    return parents, ranks


# 부모 찾기
def find_set(x):
    if x != parents[x]:
        parents[x] = find_set(parents[x])
    return parents[x]


# 3. 합칠 때
def union(x, y):
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


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    parents, ranks = make_set(N)
    # M쌍이면... 입력 어케 받아야 하농
    for i in range(M):
        x, y = arr[i * 2], arr[i * 2 + 1]
        union(x, y)

    # 중복 없애기 위해서
    groups = set()
    for i in range(1, N+1):
        # 돌아가면서 대표자 찾기
        groups.add(find_set(i))


    print(f'#{tc} {len(groups)}')
