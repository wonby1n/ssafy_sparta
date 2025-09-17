T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for tc in range(1, T + 1):
    # N : 컨테이너 수 M : 트럭 수
    N, M = map(int, input().split())

    weight = list(map(int, input().split()))
    truck = list(map(int, input().split()))

    weight.sort(reverse=True)
    truck.sort(reverse=True)

    # 화물, 트럭 인덱스
    w_idx = 0
    t_idx = 0

    cnt = 0

    # 화물 리스트나 트럭 리스트가 끝날 때까지 반복
    while w_idx < N and t_idx < M:
        # 만약 화물이 트럭이 적재 가능한 kg수보다 작거나 같으면
        if weight[w_idx] <= truck[t_idx]:
            # 화물을 넣어주고
            cnt += weight[w_idx]
            # 화물은 다음으로 넘어간다
            w_idx += 1
            t_idx += 1

        # 못넣으면 다음 화물로 넘어가자
        else:
            w_idx += 1

    print(f'#{tc} {cnt}')