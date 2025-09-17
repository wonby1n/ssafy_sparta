T = int(input())
for tc in range(1, T+1):
    # 간선 E, N
    E, N = map(int,input().split())
    # 부모 자식 입력받기
    arr = list(map(int, input().split()))

    cleft = [0] * (E+2)
    cright = [0] * (E+2)

    # 각자 인덱스에 넣어주기
    for i in range(E):
        # 엄마는 0번, 2번, 4번이니까
        p = arr[i*2]
        c = arr[i*2+1]
        # 자식은 홀수니까 홀수 입력받는데, 좌 우 순서로 오니까
        if cleft[p] == 0:
            cleft[p] = c
        else:
            cright[p] = c

    def subtree(node):
        # 노드에 암것도 없으믄 자기만.. node는 무조건 N으로 값을 받아오기 때문에 처음 함수를 호출할 땐 else문으로 가게 된다
        if node == 0:
            return 1
        # 있으면 자식 불러오기
        else:
            return 1 + subtree(cleft[node]) + subtree(cright[node])

    result = subtree(N)

    print(f'#{tc} {result}')