# 0~9 사이의 숫자 카드
# run = 연속적인 번호 / triplet = 동일한 번호
# run과 triplet으로만 구성되면 baby-gin
# 6자리의 숫자가 주어짐

cards = int(input())
card_lst = [0] * 12

# cards에 있는 정수들을 하나씩 빼서 card_lst에 넣는다
for i in range(len(cards)):
    card_lst[cards % 10] += 1
    cards //= 10

# 조건문 시작 전 구하고 싶은 변수 지정, 카드 번호 지정
i = 0
tri = 0
run = 0

while i < 10:
    if card_lst[i] >= 3:
        card_lst[i] -= 3
        tri += 1
    if card_lst[i] >= 1 and card_lst[i+1] >= 1 and card_lst[i+2]:
        card_lst[i] -= 1
        card_lst[i-1] -= 1
        card_lst[i-2] -= 1
        run += 1
        continue
    i += 1
