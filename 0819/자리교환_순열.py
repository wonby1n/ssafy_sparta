# 누구랑 자리를 바꿀래?
lst = [1,2,3]
N = 3

def make_perm(idx):

    # 종료조건
    if idx == N:
        print(lst)
        return

    # 1번이랑 누가 자리를 바꿀래?
    for i in range(idx, N):
        lst[idx], lst[i] = lst[i] = lst[idx]
        # 자리 다 바꿨으니 그다음으로 넘어가기
        make_perm(idx+1)
        # 초기화 해주기
       lst[idx], lst[i] = lst[i] = lst[idx]