def quicksort(arr, l, r):
    if l >= r:
        return
    p = partition(arr, l, r) # 피벗 위치 확정
    quicksort(arr, l, p-1) # 왼쪽 정렬
    quicksort(arr, p+1, r) # 오른쪽 정렬

def partition(arr, l, r):
    pivot = arr[l]    # 맨 왼족 원소를 피벗으로 선택
    i, j = l +1, r  # i는 왼쪽 탐색, j는 오른쪽 참색

    while True:
        while i <= j and arr[i] <= pivot: # pivot보다 큰 값을 찾을 때까지
            i += 1
        while i <= j and arr[j] >= pivot: # pivot보다 작은값을 찾을 때까지
            j -= 1
        # 위치 바꿔주기
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break

    arr[l], arr[j] = arr[j], arr[l] # pivot 제자리에 두기
    return j # pivot 최종 위치

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    quicksort(arr, 0, N-1)
    print(f'#{tc} {arr[N//2]}')