def inorder(t):
    global current
    # t가 노드 범위를 벗어나버리면 돌아오기
    if t > N:
        return
    inorder(2*t)
    tree[t] = current
    current += 1
    inorder(2*t+1)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # 이진트리 만들 리스트
    tree = [0] * (N+1)
    # 현재 노드 시작 값
    current = 1

    inorder(1)
    print(f'#{tc} {tree[1]} {tree[N//2]}')