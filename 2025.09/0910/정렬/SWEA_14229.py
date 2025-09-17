# sort 내장함수 쓰기
arr = list(map(int, input().split()))

arr.sort()
print(arr[500000])

# merge_sort 쓰기

def merge_sort(start, end):
    # 종료조건, 만약 start과 end가 같아지면
    if start == end -1:
        return

    # 반 정해주기
    mid = (start + end) // 2

    merge_sort(start, mid)
    merge_sort(mid, end)
    # 병합하기
    merge(start, mid, end)


def merge(start, mid, end):
    # 시작 인덱스 정해주기
    l, r = start, mid
    N = end-start

    # 결과 넣어줄 임시 리스트 만들기
    result = [0] * N
    idx = 0

    # 시작점이 마지막전에 도착하기 전까지 반복
    while l < mid and r < end:
        # 오른쪽에 있는게 왼쪽보다 크면
        if arr[l] < arr[r]:
            result[idx] = arr[l]
            idx += 1
            l += 1
        else:
            result[idx] = arr[r]
            idx += 1
            r += 1

    # 만약 남아잇는 게 잇으면
    while l < mid:
        result[idx] = arr[l]
        idx += 1
        l += 1

    while r < mid:
        result[idx] = arr[r]
        idx += 1
        r += 1

    # 저장하기
    for i in range(N):
        arr[start+i] = result[i]

