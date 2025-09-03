"""
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
"""

# 트리 노드의 수
N = int(input())
# 트리 정보 -> 두개씩 끊어서 읽으면 앞쪽이 부모, 뒤쪽이 자식
tree = list(map(int, input().split()))

# 부모 노드 번호를 인덱스로 사용하는 방법
cleft = [0] * (N + 1)
cright = [0] * (N + 1)

for i in range(N-1):
    # 앞이 부모
    p = tree[i * 2]
    # 뒤가 자식
    c = tree[i * 2 + 1]

    # p번 노드의 왼쪽 자식이 없다면
    if cleft[p] == 0:
        # c번 노드를 p번 노드의 왼쪽 자식으로
        cleft[p] = c
    else:
        # 왼쪽 자식이 있다면 오른쪽 자식으로
        cright[p] = c