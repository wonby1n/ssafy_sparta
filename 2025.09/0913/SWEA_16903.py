# 트럭 하나당 화물 하나
# 화물 하나도 못 옮기면 0 출력

T = int(input())
for tc in range(1, T+1):
    # N : 화물 M : 트럭
    N, M = map(int, input().split())
    # 화물 무게
    container = list(map(int, input().split()))
    # 트럭 적재용량
    truck = list(map(int, input().split()))

    container.sort(reverse=True)
    truck.sort(reverse=True)

    # 구하고 싶은 값
    total = 0
    # 컨테이너 인덱스
    c_idx = 0

    # 현재 트럭에 실을 수 있는 가장 무거운 컨테이너 넣기
    # 트럭 적재용량을 살피면서 모든 컨테이너를 다 탐색한다
    for t in truck:
        while c_idx < N:
            if container[c_idx] <= t:
                total += container[c_idx]
                c_idx += 1
                # 1트럭당 1화물만 넣을 수 있으므로
                break
            c_idx +=1 # 무거우면 다음 컨테이너 확인하러 가기