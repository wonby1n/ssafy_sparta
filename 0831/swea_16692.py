def make_tree(t):
    global cnt
    if t > N:
        return
    make_tree(2*t)
    tree[t] = cnt
    cnt +=1
    make_tree(2*t+1)


T = int(input())
for tc in range(1, T+1):
    N = int(input())

    tree = [0] * (N+1)

    cnt = 0


# 전위
def preorder(t):
    if t:
        print(t, end= ' ')
        preorder(2*t)
        preorder(2*t+1)