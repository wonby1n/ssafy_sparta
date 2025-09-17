T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(input().split())

    # 덱을 2개로 나눔
    # N이 4면 div는 2, N이 5면 div는 2
    # a = 0,1 b = 2,3
    # a = 0,1,2 b = 2,3
    div = N // 2
    first = []
    second = []
    if N % 2 == 0:
        first = arr[:div]
        second = arr[div:]
    else:
        first = arr[:div]
        second = arr[div+1:]

    # 만약 홀수면 first에게 +1 더준다

    answer = []

    for i in range(div):
        answer.append(first[i])
        answer.append(second[i])

    if N % 2 == 1:
        answer.append(arr[div])

    print(f'#{tc}', *answer)