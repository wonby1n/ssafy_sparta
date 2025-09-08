# 최대 몇 대의 화물차가 이용할 수 있는지 알아내 출력

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = []

    # (작업시작, 작업종료) 형태의 입력이 N줄
    work_list = [list(map(int, input().split())) for _ in range(N)]

    # 위에 있는 리스트를 끝나는 시간(e)를 기준으로
    # 끝나는 시간이 빠른것이 앞으로 오도록 정렬
    # 끝나는 시간 기준 오름차순 정렬
    work_list.sort(key=lambda e: e[0])

    # 최대 작업의 개수
    cnt = 0

    # 작업 종료 시간이 빠른것부터 선택
    # 현재 작업의 시작시간이 si 라고 하면
    # 이전 작업의 끝난 시간 ei-1 보다 현재 작업 시작시간이 크거나 같아야 한다

    # 이전 작업 끝난 시간
    last_end = 0
    for i in range(N):
        # i번 작업의 시작시간, 종료시간
        start = work_list[i][0]
        end = work_list[i][1]

        # i번 작업은 이전 작업의 끝시간보다
        # i번 작업의 시작시간이 크거나 같아야 한다
        if start >= last_end:
            # 이 작업을 고른다
            cnt += 1
            # 이 작업 끝난 시간
            last_end = end