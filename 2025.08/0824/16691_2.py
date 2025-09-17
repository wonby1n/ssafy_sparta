# 이진 트리 만들기
def make_tree(E, tree, cleft, cright):
    for i in range(E):
        p = tree[i*2]
        c = tree[i*2+1]

        if cleft[p] == 0:
            cleft[p] = c
        else:
            cright[p] = c

def subtree(node):
    if node == 0:
        return 0
    else:
        return 1 + subtree(cleft[node]) + subtree(cright[node])


T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    tree = list(map(int,input().split()))

    cleft = [0] * (E+2)
    cright = [0] * (E+2)

    make_tree(E, tree, cleft, cright)
    result = subtree(N)

    print(f'#{tc} {result}')