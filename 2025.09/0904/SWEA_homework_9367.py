T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    # 당근은 자기 자신은 세고 들어간다
    carrot = 1
    # 내가 구하고 싶은 max_carrot
    max_carrot = 0

    # 다음 꺼랑 비교하기 위해서 인덱스를 총 길이의 -1 해준다
    for i in range(N-1):
        # 만약 현재 당근이 다음 당근보다 작으면
        if arr[i] < arr[i+1]:
            # 1 증가시켜줌
            carrot += 1
        # 아니면
        else:
            # 당근 초기화
            carrot = 1

        # max_carrot도 갱신시켜주기
        if max_carrot < carrot:
            max_carrot = carrot

    print(f'#{tc} {max_carrot}')