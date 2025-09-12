# 요거는 재귀로 반을 나누고 합쳐주는 함수
def merge_sort(start, end):
    # 종료조건, 만약 start랑 end랑 같아지면
    if start == end - 1:
        return

    # 재귀 호출
    # mid 정해주기
    mid = (start+end)//2

    # 길이가 1이 될때까지 왼쪽 오른쪽 나눠주기
    merge_sort(start,mid)
    merge_sort(mid,end)

    # 병합하기
    merge(start,mid,end)


# 이제 반으로 나눈 걸 하나하나 비교해서 넣어줄 함수
def merge(start,mid,end):
    # 왼쪽, 오른쪽 '시작' 인덱스 정해주기
    l, r = start, mid
    N = end-start
    # 결과 넣어줄 임시 리스트 만들기
    result = [0] * N
    # 인덱스
    idx = 0
    # l, r (시작점)이 마지막에 도착할때까지 반복
    while l < mid and r < end:
        if arr[l] < arr[r]:
            result[idx] = arr[l]
            l += 1
        else:
            result[idx] = arr[r]
            r += 1
        idx += 1

    # 만약 남아있는 게 있으면
    # 넣어준다 (왼,오)
    while l < mid:
        result[idx] = arr[l]
        l += 1
        idx += 1

    while r < end:
        result[idx] = arr[r]
        r += 1
        idx += 1

    # 그다음에 result에 있는거 원본에 복사해주기
    for i in range(N):
        arr[start+i] = result[i]

arr = [25, 10, 5, 15, 20]

merge_sort(0,len(arr))
print(arr)