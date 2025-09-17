from heapq import heappop, heappush

# 프림은 우선순위큐 사용해서 푸는 거 (정점)
def cal(i, j):
    return E * ((x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2)

def prim(node):
    # 가중치, 노드
    heap = [(0,node)]
    # visited 배열
    MST = [0] * N
    # 안에서 갱신해줄 값
    min_val = 0

    while heap:
        # 빼주기
        cost, next_node = heappop(heap)

        # 만약 방문한 적이 잇다면 pass~
        if MST[next_node]:
            continue

        # 없으면
        MST[next_node] = 1
        min_val += cost

        # 이제 ㅈㄴ 어려운거 시작..
        for v in range(N):
            if not MST[v]:
                heappush(heap, (cal(next_node, v), v))

    return round(min_val)

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    # x, y 좌표가 따로 들어오므로
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    # 세율
    E = float(input())