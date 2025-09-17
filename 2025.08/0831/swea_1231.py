T = 1
for tc in range(1, 11):
    N = int(input())

    tree = [''] * (N+1)
    cleft = [0] * (N+1)
    cright = [0] * (N+1)

    for _ in range(N):
        arr = input().split()

        idx = int(arr[0])
        tree[idx] = arr[1]

        if len(arr) >= 3:
            cleft[idx] = int(arr[2])
        if len(arr) >= 4:
            cright[idx] = int(arr[3])

answer = []

def inorder(v):
    if v == 0:
        return
    inorder(cleft[v])
    answer.append(tree[v])
    inorder(cright[v])

inorder(1)
print(answer)