lst = []
for _ in range(2):
    a = int(input())
    lst.append(a)

my_lst = [2, 18]


# 3월 ~ 12월 일때
if lst[0] > my_lst[0]:
    print('After')
# 1월일때
elif lst[0] < my_lst[0]:
    print('Before')
# 2월일때
elif lst[0] == my_lst[0]:
    # 날짜가 더 클 때
    if lst[1] > my_lst[1]:
        print('After')
    elif lst[1] < my_lst[1]:
        print('Before')
    else:
        print('Special')
