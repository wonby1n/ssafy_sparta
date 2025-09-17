# 연속한 숫자가 3개 이상이면 run
# 같은 숫자가 3개 이상이면 triplet
# 교대로 한장씩 카드를 가져감

def babyjin(card_list):
    for i in range(len(card_list)):
        if card_list[i] >= 3:
            return True

    for i in range(len(card_list)-2):
        if card_list[i] >=1 and card_list[i+1] >=1 and card_list[i+2] >=1:
            return True

    return False


T = int(input())
for tc in range(1, T+1):
    cards = list(map(int, input().split()))
    N = 12

    # 플레이어 1,2가 각각 나눠가질 카드 (0~9까지)
    p1 = [0] * 10
    p2 = [0] * 10
    winner = 0

    # 카드 나눠주기
    # 플레이어 1 -> 0,2,4,6...번째 카드
    # 플레이어 2 -> 1,3,5,7...번째 카드
    for idx, val in enumerate(cards):
        # 1번째 플레이어 가져가기
        if idx % 2 == 0:
            p1[val] += 1
            if babyjin(p1):
                winner = 1
                break
        # 2번째 플레이어 가져가기
        else:
            p2[val] += 1
            if babyjin(p2):
                winner = 2
                break

    print(f'#{tc} {winner}')