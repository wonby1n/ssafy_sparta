def found_one(idx, cnt):
    global max_cnt
    # 종료
    if idx == N:
        return

    # 재귀호출
    if arr[idx] == 1:
        cnt += 1
    else:
        cnt = 0

    if max_cnt < cnt:
        max_cnt = cnt

    found_one(idx + 1, cnt)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input()))

    cnt = 0
    max_cnt = 0


    # for i in range(N):
    #     if arr[i] == 1:
    #         cnt += 1
    #     else:
    #         cnt = 0
    #
    #     if max_cnt < cnt:
    #         max_cnt = cnt
    #
    # print(max_cnt)

    found_one(0,cnt)
    print(f'#{tc} {max_cnt}')