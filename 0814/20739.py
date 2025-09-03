T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 최종 목표
    answer = 0
    for r in range(N):
        cnt = 0
        for c in range(N):
            if arr[r][c] == 1:
                cnt += 1
            else:
                if cnt >= 2:  # 구조물은 최소 2칸 이상이어야 유효
                    if answer < cnt:
                        answer = cnt
                cnt = 0
        # 행 끝났을 때 처리
        if cnt >= 2:
            if answer < cnt:
                answer = cnt

    for c in range(N):
        cnt = 0
        for r in range(N):
            if arr[r][c] == 1:
                cnt += 1
            else:
                if cnt >= 2:  # 구조물은 최소 2칸 이상이어야 유효
                    if answer < cnt:
                        answer = cnt
                cnt = 0
        # 행 끝났을 때 처리
        if cnt >= 2:
            if answer < cnt:
                answer = cnt

    print(f'#{tc} {answer}')