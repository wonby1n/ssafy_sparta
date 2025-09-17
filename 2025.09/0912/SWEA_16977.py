def bus_charge(now_bus, cnt):
    global charge_cnt

    if cnt >= charge_cnt:
        return

    # 종료조건. 만약 버스가 종점에 도착하면
    if now_bus >= N-1:
        charge_cnt = min(cnt, charge_cnt)
        return

    for b in range(bus_stop[now_bus], 0, -1):
        bus_charge(now_bus+b, cnt+1)


T = int(input())
for tc in range(1, T+1):
    N, *bus_stop = map(int, input().split())

    charge_cnt = 100 * N

    bus_charge(0,0)

    print(f'#{tc} {charge_cnt-1}')