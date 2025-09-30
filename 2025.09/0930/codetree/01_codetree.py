X, Y = map(int, input().split())

max_sum = -1

for n in range(X, Y + 1):
    # 숫자를 문자열로 바꿔서 각 자리 숫자를 int로 변환 → sum으로 합 구함
    digit_sum = sum(map(int, str(n)))

    max_sum = max(digit_sum, max_sum)

print(max_sum)
