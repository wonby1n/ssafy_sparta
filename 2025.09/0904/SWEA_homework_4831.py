# 버스는 0번에서 출발해 종점인 N번 정류장까지 이동
# K : 최대한 이동할 수 있는 정류장
# N : 종점 정류장
# M : 충전기 설치된 정류장 번호
# 몇 번의 충전을 해야 종점에 도착할 수 있는지?
# 도착할 수 없는 경우 : 0

T = int(input())
for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    lst = list(map(int, input().split()))

    # visited 배열 만들어둔다

    stop_list = [0] * (N+1)
    for i in lst:
        stop_list[i] = 1

    # 버스가 마지막으로 충전하게 되는 지점
    last = 0
    # 버스가 최대로 움직인 위치
    bus = K
    # 충전 횟수, 시작충전은 횟수 제외
    cnt = 0

    possible = True
    # 버스 위치가 종점 정류장에 가기 전까지
    while bus < N:
        # 만약 stop_list가 0이면, 버스를 최대 위치에서 1을 빼준다
        while stop_list[bus] == 0:
            bus -= 1
            # 만약에 발견 못하고 마지막 위치로 돌아가면?
            if bus == last:
                possible = False
                break
        if not possible:
            cnt = 0
            break

        # stop_list[bus] == 1, 충전소를 찾았다면
        # 마지막 충전 위치 갱신
        last = bus
        # 충전 횟수도 +1
        cnt += 1
        # 다시 K칸 전진해서 보기
        bus += K

    print(f'#{tc} {cnt}')