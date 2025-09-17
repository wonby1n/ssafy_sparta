# 스도쿠 9x9
T = 10
for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]

    valid = 1  # 기본값은 유효(1)로 시작

    # 행 순환
    for r in range(9):
        dup = []  # 현재 행의 중복값 저장

        for c in range(9):  # 첫 번째 비교 위치
            for i in range(c + 1, 9):  # 두 번째 비교 위치
                if arr[r][c] == arr[r][i]:  # 값이 같으면
                    real = False

                    # 이미 dup에 있는지 확인
                    for k in range(len(dup)):
                        if dup[k] == arr[r][i]:
                            real = True
                    if not real:
                        dup.append(arr[r][i])

        # 만약 중복이 발견되면, valid를 0으로 바꾸고 반복 종료
        if len(dup) > 0:
            valid = 0
            break

    # 행 순환
    for r in range(9):
        dup = []  # 현재 행의 중복값 저장

        for c in range(9):  # 첫 번째 비교 위치
            for i in range(c + 1, 9):  # 두 번째 비교 위치
                if arr[r][c] == arr[r][i]:  # 값이 같으면
                    real = False

                    # 이미 dup에 있는지 확인
                    for k in range(len(dup)):
                        if dup[k] == arr[r][i]:
                            real = True
                    if not real:
                        dup.append(arr[r][i])

        # 만약 중복이 발견되면, valid를 0으로 바꾸고 반복 종료
        if len(dup) > 0:
            valid = 0
            break