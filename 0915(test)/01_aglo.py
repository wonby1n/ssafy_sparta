T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())

    arr = list(map(int, input().split()))

    ##############################
    # arr를 M개씩 잘라서 부분수열을 만든다
    # m개의 숫자가 증가하는 패턴인가?
    # 증가하는 패턴의 개수를 구하면 되는 문제다

    count = 0

    # 배열을 m개씩 잘랐을때 각 부분 수열의 시작위치(인덱스)를 i라고 하면
    for i in range(0, N, M):
        # 시작위치 i를 기준으로 해서 M개 잘라내기
        subarr = arr[i:i + M]

        # 이 잘라낸 subarr가 단순증가패턴인가?
        # 증가한다
        increase = True

        # 이 부분배열의 중간에서 증가하지 않은적이
        # 한 번이라도 있다면? 증가패턴이 아님
        for j in range(len(subarr)):
            # 앞에있는 원소가 j, 뒤에있는 원소가 j+1
            if subarr[j] >= subarr[j + 1]:
                increase = False
                break
        # 반복이 끝나고 나서 increase가 그대로 있으면
        if increase:
            # 이 패턴은 증가 패턴이다
            count += 1

    print(count)
