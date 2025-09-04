# 교환횟수 k를 단계로
def solve(k):
    global numbers, max_price, check, cnt, N
    # 가지치기
    # k번 교환해서 만든 숫자열을 이전에 만든 적이 있다면:
    current_number = "".join(numbers)
    
    if (k, current_number) in check:
        return
    check.add((k, current_number))

    # 종료
    if k == cnt:
        max_price = max(max_price, int(current_number))
        return

    # 재귀호출(다음단계)
    # 자리를 교환해서 다음 단계(다음 교환횟수)
    # 앞쪽자리 인덱스 i : 0 ~ N
    # 뒤쪽자리 인덱스 j : i+ 1 ~ N-1
    for i in range(N-1):
        for j in range(i+1, N):
            # i와 j를 정해서 자리바꾸기
            numbers[i], numbers[j] = numbers[j], numbers[i]
            # 자리 바꾼 다음에 다음 교환횟수로 -> 재귀호출, 교환횟수 +1
            solve(k + 1)
            # i와 j를 바꿔서 원상복귀
            numbers[i], numbers[j] = numbers[j], numbers[i]

T = int(input())
for tc in range(1, T+1):
    # numbers : 처음 숫자, cnt : 교환 횟수
    numbers_str, cnt_str = input().split()

    # 교환횟수
    cnt = int(cnt_str)
    N = len(numbers_str)
    numbers = list(numbers_str)

    max_price = 0

    # 세트 안에는 (교환 횟수 k, k번 교환해서 만든 숫자열) 튜플로 저장
    # 3번의 교환을 통해서 '12345' 라는 숫자열을 이전에 만든 적이 있다면
    # 나중에 교환순서는 다르지만 3번 교환을 통해 '12345'를 만들면
    # 여기서 다시 만드는 모든 숫자열은 중복이 된다
    check = set()

    # 교환 안했으니 교환횟수 0부터 시작
    solve(0)

    print(f'#{tc} {max_price}')