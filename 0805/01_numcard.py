T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input()))

    # 빈 리스트 만듦
    num = [0] * 10
    # 1. 가장 많은 카드에 적힌 숫자
    # 2. 카드가 몇 장인지 출력
    # 3. 카드 장수가 같을 때는 숫자가 큰 쪽
    # 일단 카드에 적힌 숫자들의 개수를 센다
    # num[0] -> 1 이면, 0번 숫자는 1개의 카드만 있다는 뜻
    for i in arr:
        num[i] += 1

        # 원하는 값 리스트
        max_val = num[0]
        max_num = 0

        # num에서 가장 큰 값의 위치(인덱스)를 찾아야 함
        for j in range(len(num)):
            if max_val < num[j]:
                max_val = num[j]
                max_num = j
            elif max_val == num[j] and max_num < j:
                max_num = j

    print(f'#{test_case} {max_num} {max_val}')