def binary_serch(traget):
    left, right = 0, len(arr)-1 # 검색 시작, 끝점
    cnt = 0 # 검색 횟수

    while left <= right: # 교차되면 탐색 종료
        mid = (left + right) // 2
        cnt += 1

        if arr[mid] == traget: # 반으로 나눈 게 정답이다! (정답 바로 찾음)
            return mid, cnt
        elif target < arr[mid]: # 정답이 왼쪽구간에 있으면 (mid보다 작으면)
            right = mid - 1
        else: # 정답이 오른쪽 구간에 있으면 (mid보다 크면)
            left = mid + 1

    return -1, cnt # 못찾으면
