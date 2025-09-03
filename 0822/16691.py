# 트리 만들기
def make_tree(E, tree, cleft, cright):
    # 간선 개수만큼 돌기
    for i in range(E):
        # 부모
        p = tree[i*2]
        # 자식
        c = tree[i*2+1]
        # 부모의 왼쪽과 오른쪽에 자식 추가하기
        if cleft[p] == 0:
            cleft[p] = c
        else:
            cright[p] = c
    return cleft, cright

# 서브트리 노드 수 세기
def count_node(node):
    # 만약 노드가 존재하지 않는다면
    if node == 0:
        return 0
    # 존재한다면, 현재 노드 수 1 + 왼쪽 + 오른쪽
    return 1 + count_node(cleft[node]) + count_node(cright[node])


T = int(input())
for tc in range(1, T + 1):
    # E 간선 N 시작 노드
    E, N = map(int, input().split())
    tree = list(map(int, input().split()))

    cleft = [0] * (E + 2)
    cright = [0] * (E + 2)

    cleft, cright = make_tree(E, tree, cleft, cright)

    result = count_node(N)
    print(f'#{tc} {result}')