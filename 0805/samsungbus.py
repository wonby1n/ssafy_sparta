# 문제: 각 버스 정류장(Cj)을 지나는 버스 노선 개수를 구하는 문제
# 버스 정류장은 1번부터 5000번까지 있고,
# 각 버스 노선은 (Ai, Bi) 범위 내 모든 정류장을 다님

# 카운트 정렬로 가보자

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    # 버스 정류장 (정류장 번호: 1 ~ 5000)
    bus_stop = [0] * 5001

    # 각 버스 노선 범위만큼 카운트 +1
    for _ in range(N):
        Ai, Bi = map(int, input().split())
        for i in range(Ai, Bi + 1):  # 해당 노선이 지나는 모든 정류장
            bus_stop[i] += 1

    P = int(input())  # 확인할 정류장 개수

    bus_c = []  # 확인할 정류장 번호 리스트
    for _ in range(P):
        Cj = int(input())
        bus_c.append(Cj)

    # 결과 저장용 리스트
    result = []
    for c in bus_c:
        result.append(bus_stop[c])

    print(f'#{tc}', *result)