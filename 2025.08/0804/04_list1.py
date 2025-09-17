T = int(input())
for test_case in range(1, T + 1):
    # N개의 건물, 건물의 높이
    N = int(input())
    tower = list(map(int, input().split()))

    # 정답에 넣을 변수값을 0으로 설정
    result = 0
    # 내 양옆 건물 2개씩을 비교해야 함
    # 그러므로 비교대상은 2번째 위치하는 것부터 시작하면 됨
    # 그리고 마지막은 N-2 (왜냐면 N번째에 있는 거의 +2개까지 구해야 하므로)
    for i in range(N-2):
        # 현재 건물의 높이를 저장함
        my_tower = tower[i]
        # 나(i)랑, 내 양옆에 있는 거 두개씩 비교함
        # 그러기 위해서는 양옆에 있는 값을 가져와야 함

        left2 = tower[i-2]
        left1 = tower[i-1]
        right1 = tower[i+1]
        right2 = tower[i+2]

        # 제일 큰 빌딩 값을 구한다
        max_tower = left2
        if max_tower < left1:
            max_tower = left1
        if max_tower < right1:
            max_tower = right1
        if max_tower < right2:
            max_tower = right2

        if my_tower > max_tower:
            result += my_tower - max_tower

    print(f'#{test_case} {result}')