N = int(input())
N_lst = list(map(int, input().split()))
M = int(input())
M_lst = list(map(int, input().split()))

for num in M_lst:
    if num in N_lst:
        print(1)
    else:
        print(0)