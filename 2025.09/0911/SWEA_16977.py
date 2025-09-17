def bus_charge(now_bus, cnt):
    global min_val
    # 가지치기. 만약 현재 cnt가 min_val보다 많으면 종료
    if cnt >= min_val:
        return

    # 종료조건. 만약 마지막에 도착하면? 종료.
    if now_bus >= N-1:
        min_val = min(min_val, cnt)
        return

    # 현재부터 앞으로 갈 수 있는 경우 탐색
    for c in range(bus_stop[now_bus], 0, -1):
        bus_charge(now_bus+c, cnt+1)

T = int(input())
for tc in range(1, T+1):
    # N : 정류장 수, N-1 까지 정류장별 배터리
    N, *bus_stop = map(int ,input().split())
    min_val = float('inf')

    bus_charge(0, 0)

    print(f'#{tc} {min_val-1}')