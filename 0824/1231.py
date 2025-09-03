for tc in range(1, 11):
    N = int(input().strip())

    # 문자 저장하기
    tree = [''] * (N+1)

    left = [0] * (N+1)
    right = [0] * (N + 1)

    for _ in range(N):
        parts = input().split()

        # 첫 토큰 : 번호, 둘째 토큰 : 문자
        idx = int(parts[0])
        tree[idx] = parts[1]

        # 입력된 parts가 3개면 : 왼쪽 자식만 있음
        # 입력된 parts가 4개면 : 왼쪽, 오른쪽 둘 다 있음
        # 작으면 없으니까 추가 안해도 됨
        if len(parts) >= 3:
            left[idx] = int(parts[2])
        if len(parts) >= 4:
            right[idx] = int(parts[3])

    answer = []

    # 중위순회 하기
    def inorder(t):
        # 노드가 유효한지 확인하기
        if t == 0:
            return
        # 왼쪽 서브트리 방문
        inorder(left[t])
        # 현재 노드의 문자 추가
        answer.append(tree[t])
        # 오른쪽 서브트리 방문
        inorder(right[t])

    inorder(1)

    print(f'#{tc} {"".join(answer)}')