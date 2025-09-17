# 런 구하는 함수
def babygin(lst):
    for i in range(10):
        if lst[i] >= 3:
            return True

    # 789와 같이 3개짜리 런을 확인해야 하므로 8까지
    for i in range(8):
        if lst[i] >0 and lst[i+1] >0 and lst[i+2] >0:
            return True

    return False


T = int(input())
for tc in range(1, T + 1):
    cards = list(map(int, input().split()))

    # 플레이어 1, 2가 가져갈 카드 저장하기
    # 숫자에 해당하는 인덱스로 저장해서, 바로 확인할 수 있게
    p1 = [0] * 10
    p2 = [0] * 10
    winner = 0

    # 12장의 카드를 가져감
    for i in range(12):
        x = cards[i]
        # 플레이어 1 시작
        if i % 2 == 0:
            p1[x] += 1
            if len(p1) >= 3 and babygin(p1):
                winner = 1
                break
        # 플레이어 2 시작
        if i % 2 == 1:
            p2[x] += 1
            if len(p2) >= 3 and babygin(p2):
                winner = 2
                break

    print(f'#{tc} {winner}')