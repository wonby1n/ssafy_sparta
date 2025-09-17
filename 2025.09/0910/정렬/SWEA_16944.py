# 정렬 대상 리스트
arr = []

# 병합정렬 함수
# 정렬할 범위를 지정(시작, 종료)

# start에서 end까지 정렬하는 함수
def merge_sort(start, end):
    global cnt
    # 원소가 1개 이하라면 더 이상 쪼갤 수 없음 (재귀 종료 조건)
    if end - start <= 1:
        return

    # 중간 지점 계산 (배열을 반으로 나누기 위한 기준점)
    mid = (start+end) // 2

    # 왼쪽범위 정렬
    merge_sort(start, mid)
    # 오른쪽범위 정렬
    merge_sort(mid, end)

    # 합치기 전에 마지막이 큰지 확인하기
    if arr[mid-1] > arr[end-1]:
        cnt += 1
    # 합치기
    merge(start, mid, end)

def merge(start, mid, end):
    # 왼쪽, 오른쪽 시작 인덱스 정해주기
    l, r = start, mid

    # 결과 배열 길이 (두 구간 합친 크기)
    N = end - start
    # 결과 저장 배열
    result = [0] * N

    # 결과 배열을 채울 인덱스
    idx = 0

    # 두 구간을 동시에 비교하며 작은 값을 결과 배열에 채움
    while l < mid and r < end:
        if arr[l] < arr[r]:
            result[idx] = arr[l] # 왼쪽 값이 더 작으면 결과에 저장
            l += 1               # 왼쪽 포인터 이동
        else:
            result[idx] = arr[r] # 오른쪽 값이 더 작으면 결과에 저장
            r +=1                # 오른쪽 포인터 이동
        idx += 1                 # 결과 배열 인덱스 이동

    # 값이 남아 있는 경우

    # 왼쪽 구간
    while l < mid:
        result[idx] = arr[l]
        l += 1
        idx += 1

    # 오른쪽 구간
    while r < end:
        result[idx] = arr[r]
        r += 1
        idx += 1

    # 정렬된 결과 배열을 원본 배열에 덮어쓰기
    for i in range(N):
        arr[start+i] = result[i]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    merge_sort(0, len(arr))

    print(f'#{tc}',arr[N//2], cnt)