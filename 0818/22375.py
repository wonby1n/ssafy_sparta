T = int(input())
for tc in range(1, T+1):
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # 현재 상태가 000 이고 조작 후 상태가 010인 경우
    # 초기상태 000에서 2번 스위치를 조작하면 011
    # 3번 스위치를 조작하면 010 -> 2번 작동시켜야 함

    # 구하고 싶은 값
    cnt = 0
    # 스위치의 상태를 비교할 거임
    for i in range(N):
        # 만약 i번째 스위치가 다르면
        if A[i] != B[i]:
            # 스위치 조작할거니까 cnt 때려주고
            cnt += 1
            # i번째부터 마지막까지 뒤집어줘야 함
            for j in range(i, N):
                if A[j] == 1: # 1이면
                    A[j] = 0
                else:
                    A[j] = 1
