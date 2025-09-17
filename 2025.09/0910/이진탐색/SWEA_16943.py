def binary(target):
    left, right = 0, A - 1
    dir = 0  # 0=시작, -1=왼쪽, 1=오른쪽

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:  # 바로 찾으면 조건 만족
            return 1

        if target < arr[mid]:  # 왼쪽으로 가야 함
            if dir == -1:  # 이전에도 왼쪽 갔으면 불만족
                return 0
            dir = -1
            right = mid - 1
        else:  # 오른쪽으로 가야 함
            if dir == 1:  # 이전에도 오른쪽 갔으면 불만족
                return 0
            dir = 1
            left = mid + 1

    return 0


T = int(input())
for tc in range(1, T + 1):
    A, B = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()  # 이진탐색은 반드시 정렬된 배열에서!
    brr = list(map(int, input().split()))

    result = 0
    for i in brr:
        result += binary(i)

    print(f'#{tc} {result}')