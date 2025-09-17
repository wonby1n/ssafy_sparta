# 각 행과 열이 중복되면 안 됨
# 순열
def recur(start, visited, now_sum):
    global battery
    # 가지치기. 현재 구한 값이 그전 구한 값보다 크면
    if now_sum >= battery:
        return

    # 모든 구역에 방문완료하면
    if len(visited) == N:
        now_sum += company[start][0] # 다시 1번(인덱스는 0) 사무실 복귀
        battery = min(battery, now_sum)
        return

    for next_area in range(1, N): # 0은 제외
        # visited 배열에 없으면
        if next_area not in visited:
            # 반복문
            recur(next_area, visited + [next_area], now_sum + company[start][next_area])


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    company = [list(map(int, input().split())) for _ in range(N)]

    # 구하고 싶은 거 : 최소 배터리 사용량
    battery = float('inf')

    # 열 사용 여부 체크
    used = [0] * N

    # 0번(사무실)부터 시작
    recur(0,[0],0)

    print(f'#{tc} {battery}')