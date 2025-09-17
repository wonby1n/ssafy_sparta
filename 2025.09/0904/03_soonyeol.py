arr = [1,2,3]
N = len(arr)

P = [0] * N
used = [0] * N
# 3장을 뽑아서 순열 만들기
def perm(idx):
    # 종료
    if idx == N:
        print(P)
        return
    # 재귀호출
    # idx번 자리에는 어떤 카드를 놓을지
    for i in range(N):
        # idx번 자리에는 i번 카드를 놓을거다
        # i번 카드는 이전에 놓은적이 없어야 한다
        if not used[i]:
            P[idx] = arr[i] # 순열의 idx번 자리는 arr의 i번 카드를 놓겠다.
            used[i] = 1 # i번 카드는 사용했다 라고 표시
            perm(idx+1) # 순열의 idx+1번 자리에 대해서 결정하러 가기
            used[i] = 0 # i번 카드를 사용한 적이 없다 라고 다시 표시

# 순열의 0번 자리에 어떤 카드를 놓을것인가?부터 시작
perm(0)
