# 최대 몇 대의 화물차가 이용할 수 있는지 알아내 출력

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = []
    for _ in range(N):
        a, b = map(int, input().split())
        arr.append([a,b])

    # 끝나는 시간 기준으로 정렬하기 (그냥 정렬하면 안 됨)
    arr.sort(key=lambda x: x[1])

    # 시작점 설정하기
    cnt = 1
    truck = arr[0][1]

    # 두번째 화물차부터 확인
    for i in range(1, N):
        # 현재 화물차의 시작 시간이 이전에 선택한 화물차의 끝나는 시간보다 크거나 같으면 선택
        if arr[i][0] >= truck:
            cnt += 1
            truck = arr[i][1]

    print(f'#{tc} {cnt}')