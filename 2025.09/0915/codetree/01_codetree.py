def solution():
    N, M = map(int, input().split())

    # A와 B의 이동 경로를 각각 저장할 리스트
    # 최대 1,000,000초까지의 위치를 기록할 수 있도록 충분히 큰 크기로 설정
    a_pos = [0] * 1000001
    b_pos = [0] * 1000001

    a_time = 1
    # A의 이동 경로 기록
    for _ in range(N):
        direction, move_time = input().split()
        move_time = int(move_time)
        for _ in range(move_time):
            if direction == 'R':
                a_pos[a_time] = a_pos[a_time - 1] + 1
            else:  # direction == 'L'
                a_pos[a_time] = a_pos[a_time - 1] - 1
            a_time += 1

    b_time = 1
    # B의 이동 경로 기록
    for _ in range(M):
        direction, move_time = input().split()
        move_time = int(move_time)
        for _ in range(move_time):
            if direction == 'R':
                b_pos[b_time] = b_pos[b_time - 1] + 1
            else:  # direction == 'L'
                b_pos[b_time] = b_pos[b_time - 1] - 1
            b_time += 1

    a_total_time = a_time - 1
    b_total_time = b_time - 1

    # 두 사람의 이동이 모두 끝난 시간까지 확인
    max_time = max(a_total_time, b_total_time)

    # 처음 만나는 시간 찾기
    for t in range(1, max_time + 1):
        if a_pos[t] == b_pos[t]:
            print(t)
            return

    # 만약 루프가 끝날 때까지 만나지 않았다면 -1 출력
    print(-1)


solution()