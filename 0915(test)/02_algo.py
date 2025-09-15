
T = int(input())


# idx : 현재 단계
# selected : 지금까지 고른 사과 번호 체크
# 현재 단계에서 어떤 사과를 골랐을때 거리 계산
# 이전에 고른 사과의 위치를 알고 있어야 현재 위치와 차이 계산 가능
# location -> 위치 정보
# distance : 현재 단계까지 왔을 때 거리
def pick_apple(idx, selected, location, distance):
    global min_d
    if distance > min_d:
        return
    # 종료 조건
    if idx == N:
        # 마지막 사과를 골랐으면 되돌아가는 거리까지 추가하고
        # 이전까지의 최솟값과 현재 구한 최솟값 중에 작은것 선택
        min_d = min(distance + abs(location[0] - 0) + abs(location[1] - 0), min_d)
        return

    # N개의 사과중에 이전에 고르지 않은 i번 사과를 선택하고 다음단계
    for i in range(N):
        # i번 사과를 이전에 고른적이 없다면 현재 단계에서 선택하자
        if not selected[i]:
            # i번 사과 선택 표시
            selected[i] = 1
            # i번 사과를 골랐을때, 이전 위치와의 거리 차이
            d = abs(location[0] - apples[i][0]) + abs(location[1] - apples[i][1])
            # idx+1 단계로, 고른 사과들 상태, i번 사과 위치로 이동, 거리 d 추가
            pick_apple(idx + 1, selected, apples[i], distance + d)
            # i번 사과 선택 취소
            selected[i] = 0


for tc in range(1, T + 1):
    N = int(input())

    apples = [list(map(int, input().split())) for _ in range(N)]

    min_d = float('inf')

    pick_apple(0, [0] * N, [0, 0], 0)

    print(f'#{tc} {min_d}')