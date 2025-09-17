# N=2a x 3b x 5c x 7d x 11e (제곱임)
# N이 주어질 때 a, b, c, d, e 를 출력
T = int(input())
for test_case in range(1, T + 1):

    N = int(input())

    # 그렇다면 나머지가 생기지 않게 나눠주는 것이 중요함
    count_2 = 0
    count_3 = 0
    count_5 = 0
    count_7 = 0
    count_11 = 0

    # 다 나눠서 1이 될때까지..
    while N != 1:
        if N % 2 == 0:
            count_2 += 1
            N //= 2
        elif N % 3 == 0:
            count_3 += 1
            N //= 3
        elif N % 5 == 0:
            count_5 += 1
            N //= 5
        elif N % 7 == 0:
            count_7 += 1
            N //= 7
        elif N % 11 == 0:
            count_11 += 1
            N //= 11

    print(count_2, count_3, count_5, count_7, count_11)