from heapq import heappop, heappush


def cal(i,j):
    # i번 섬과 j번 섬 사이의 비용
    return E * ((x[i]-x[j])**2+(y[i]-y[j])**2)

def prim():
    # 그 뭐고 환경 부담금, 좌표
    heap = [(0,0)]
    MST = [0] * N
    min_val = 0

    while heap:
        value, next_node = heappop(heap)

        # 간 적 있으면 건너뛰기
        if MST[next_node]:
            continue

        # 없으면
        MST[next_node] = 1
        min_val += value

        for v in range(N):
            # 만약 방문하지 않앗다면
            if not MST[v]:
                # 힙에 환경부담금 계산한거랑, 좌표 넣는다
                heappush(heap, (cal(next_node,v),v))

    return round(min_val)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # x좌표 y좌표가 각각 따로 들어옴
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    # 환경부담금 세율
    E = float(input())

    result = prim()
    print(f'#{tc} {result}')