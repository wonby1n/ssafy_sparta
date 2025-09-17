T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 최종 정답 개수
    answer = 0

    # [가로 탐색] 각 행에서 연속한 1의 길이가 정확히 K인지 세기
    for r in range(N):
        # 현재 행에서 연속 1의 길이를 센다
        cnt = 0
        for c in range(N):
            # 현재 칸이 1이면 연속 길이를 1 증가
            if arr[r][c] == 1:
                cnt += 1
            # 현재 칸이 0이면 지금까지의 연속이 끝났으므로 길이가 K인지 확인하고 초기화
            else:
                if cnt == K:
                    answer += 1
                cnt = 0
        # 행이 1로 끝났을 때 마지막 연속 구간도 확인
        if cnt == K:
            answer += 1

    # [세로 탐색] 각 열에서 연속한 1의 길이가 정확히 K인지 세기
    for c in range(N):
        # 현재 열에서 연속 1의 길이를 센다
        cnt = 0
        for r in range(N):
            # 현재 칸이 1이면 연속 길이를 1 증가
            if arr[r][c] == 1:
                cnt += 1
            # 현재 칸이 0이면 지금까지의 연속이 끝났으므로 길이가 K인지 확인하고 초기화
            else:
                if cnt == K:
                    answer += 1
                cnt = 0
        # 열이 1로 끝났을 때 마지막 연속 구간도 확인
        if cnt == K:
            answer += 1

    print(f'#{tc} {answer}')