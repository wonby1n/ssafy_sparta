# 1부터 12까지의 숫자를 원소로 가진 집합 A
# N개의 원소, 합이 K
# 답 : 부분집합의 개수 (없으면 0)
def recur(idx, cnt):
    global result_cnt
    # 종료조건, 모든 idx를 확인하면
    if idx == 12:
        if len(cnt) == N and sum(cnt) == K:
            result_cnt += 1
        return

    # 포함하고, 안하고
    recur(idx+1, cnt + [arr[idx]])
    recur(idx+1, cnt)

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())

    # 집합 a
    arr = [1,2,3,4,5,6,7,8,9,10,11,12]

    # 답
    result_cnt = 0
    recur(0,[])
    print(result_cnt)