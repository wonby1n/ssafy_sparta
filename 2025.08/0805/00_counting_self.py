N = int(input())
arr = list(map(int, input()))

def counting_sort(data, temp, k):
    # 초기값 설정 (빈 리스트 만들기)
    count = [0] * (k+1)

    # 일단 arr에 있는 원소를 하나하나 꺼내온다.
    # 그리고 count에 있는 인덱스와 동일한 숫자가 있을 때마다 해당 인덱스에 1 증가시킨다
    for i in arr:
        count[i] += 1



    # 리스트 맨 뒤부터 꺼내서 자리를 특정해준다.
    # 나오는 숫자까지의 누적합에 -1을 해주면 마지막 자리에 넣을 수 있음
    # 자리(인덱스) = COUNT[숫자] - 1
    for i in range(len(arr)-1, -1, -1):
        # x라는 정수의 자리를 찾고 싶음
        x = arr[i]
        # count에서 arr[i]에 있는 숫자의 값을 확인, -1 한 자리가 정렬 후 위치
        count[x] -= 1
        # 정렬 후 결과 배열 temp에 arr[i] 놓기
        # x : arr[i]
        # count[x] : x(arr[i])가 들어갈 위치(인덱스)
        temp[count[x]] = x

        # 또는 이런 방법도 있음
        # count[arr[i]] -= 1
        # temp[count[arr[i]]] = arr[i]



