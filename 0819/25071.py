N = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input()))

    # 원하는 값
    step = 0
    # 현재 위치
    now = 1
    # 현재 인덱스 (=now와 같아짐)
    i = 0

    # 얼마나 이동해야 되는지 모르니까 while문
    # 현재 위치가 N이 되기 전까지 반복
    while now < N-1:
        if arr[i] == 0:
            step += 1
            now += 1
            i +=1
        else:
            step += 1
            now = arr[i] -1
            arr[i] = 0
            i = now