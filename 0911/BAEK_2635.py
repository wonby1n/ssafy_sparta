# def recur(num, cnt, path):
#     global max_cnt, answer
#     # 종료조건. 만약 num이 0보다 작거나 같으면
#     if num <= 0:
#         max_cnt = max(max_cnt, cnt)
#         return
#
#
#     # 재귀? 쨌든 뭐 만들어보자
#     for i in range(1,N-1):
#         recur(num - i, cnt+1, answer.append(num-i))
#

N = int(input())

max_cnt = 0
answer = []

for i in range(1, N):
    kijun = [N, N-i]
