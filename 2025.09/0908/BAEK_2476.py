def money(lst):
    # 세 주사위의 눈이 모두 같은 경우
    if lst[0] == lst[1] and lst[1] == lst[2]:
        return 10000 + (lst[0] * 1000)

    # 두 주사위의 눈이 같은 경우
    elif lst[0] == lst[1] or lst[1] == lst[2] or lst[0] == lst[2]:
        # 두 개가 같은 눈을 찾기 위해 set을 사용
        unique_nums = list(set(lst))
        for num in unique_nums:
            if lst.count(num) == 2:
                return 1000 + (num * 100)

    # 세 주사위의 눈이 모두 다른 경우
    else:
        return max(lst) * 100


N = int(input())
max_money = 0

for _ in range(N):
    p = list(map(int, input().split()))
    current_money = money(p)
    if current_money > max_money:
        max_money = current_money

print(max_money)