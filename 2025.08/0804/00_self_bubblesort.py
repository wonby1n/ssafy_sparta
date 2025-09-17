def bubble_sort(numbers, n):
    # numbers : 정렬하고 싶은 배열(리스트)
    # n : 배열(리스트)의 길이

    # 정렬은 자리 정하기
    # 버블정렬은 오름차순 기준으로
    # 가장 큰 원소의 자리는 마지막(N-1)
    # 마지막 자리부터 자리의 주인이 누군지 정한다.
    # 자리 번호를 i라고 하자
    for i in range(n-1, 0, -1):
        # 1번 인덱스에 누가 와야 할까를 정하는 과정
        # 맨 앞에서부터 원소 두개씩 비교를 하며
        # 작은게 왼쪽에 있고, 큰게 오른쪽에 있도록
        # 큰 원소는 왼쪽에 있으면 안된다.
        # => 왼쪽과 오른쪽 원소의 자리를 바꾼다.

        # 0번부터 i-1까지 비교를 하며 구한다.
        for j in range(i):
            # j번 인덱스에 있는 원소와 j+1번 인덱스에 있는 원소를 비교해서
            # 큰 게 왼쪽에 있으면 자리바꾸기
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j + 1] = numbers[j+1], numbers[j]

                # temp = numbers[j]
                # numbers[j] = numbers[j+1]
                # numbers[j+1] = numbers[j]