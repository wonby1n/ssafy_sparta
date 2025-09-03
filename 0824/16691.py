def make_tree(E, tree, cleft, cright):
    # 간선 개수만큼 반복하기
    for i in range(E):
        # 부모는 tree 리스트에 짝수인덱스에 있는 애들
        p = tree[i*2]
        # 자식은 tree 리스트에 홀수인덱스에 있는 애들
        c = tree[i*2+1]
    # 왼쪽과 오른쪽에 자식 추가하기
    # 왼쪽부터 먼저 주어지니까, 왼쪽이 없으면 c 추가. 왼쪽 있으면 오른쪽에 c 추가
        if cleft[p] == 0:
            cleft[p] = c
        else:
            cright[p] = c
    return cleft, cright

def subtree(node):
    # 만약 노드가 없다면
    if node == 0:
        return 0
    else:
        return 1 + subtree(cleft[node]) + subtree(cright[node])


T = int(input())
for tc in range(1, T+1):
    # 간선의 개수, 루트시킬 노드 N
    E, N = map(int, input().split())
    # 2개씩 끊어서 받음
    tree = list(map(int, input().split()))

    # 왼쪽, 오른쪽 자식 빈리스트를 만들어두자
    cleft = [0] * (E+2)
    cright = [0] * (E+2)

    make_tree(E, tree, cleft, cright)
    result = subtree(N)

    print(f'#{tc} {result}')