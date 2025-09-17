# 이진 탐색 트리는 어떤 경우에도 저장된 값이 왼쪽 서브트리의 루트 <현재 노드 <오른쪽 서브 트리의 루트인 규칙을 만족한다.
# 완전 이진 트리 형태
def make_tree(t):
    global cnt
    # 만약 현재 번호가 n보다 커버리면 리턴하즈아
    if t > N:
        return
    # 왼쪽 자식(짝수) 방문해보기
    make_tree(2*t)
    # 현재 노드에 값 채우기
    tree[t] = cnt
    # 채웠으면 1더해주기
    cnt += 1
    # 오른쪽 놈이 있나 확인
    make_tree(2*t+1)


T = int(input())
for tc in range(1, T+1):
    N = int(input())

    # 인덱스 1부터 저장하기 위해서
    tree = [0] * (N+1)

    # 현재 인덱스에 넣어질 번호
    cnt = 1