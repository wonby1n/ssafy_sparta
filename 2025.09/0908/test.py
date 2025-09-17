arr = [-1,3,-9,6,7,-6,1,5,4,-2]
N = len(arr)

# def recur(idx, sum_val):
#     # 종료 조건
#     if
#
#     # 재귀 구현
#     for i in range(1<<N):
#         for j in range(N):
#             recur(i, sum_val + arr[j])
#
#
# recur(0, 0)


# 1. 내가 푼 거
# 부분집합을 구하는 재귀함수
# idx번 인덱스에 있는 원소를 부분집합에 포함o or 포함x
def subset(cnt, result):
    # 종료조건
    # 10번 선택을 모두 완료 -> 종료
    # 그 중에 합이 0인 부분집합만 골라서 출력
    if cnt == N:
        if sum(result) == 0:
            print(*result)
            return
        return
    # 재귀호출
    # 2가지로 나뉨
    # idx번 원소를 부분집합에 포함하고 idx+1 단계로 이동
    subset(cnt+1, result + [arr[cnt]])
    # idx번 원소를 부분집합에 포함하지 않고 idx+1 단계로 이동
    subset(cnt+1, result)

subset(0, [])


# 2. 강사님 버전
# 부분집합을 구하는 재귀함수
# idx번 인덱스에 있는 원소를 부분집합에 포함o or 포함x
# selected : 우리가 지금까지 포함한 원소들
cnt = 0
def subset(idx, selected):
    global cnt
    # 종료조건
    # 10번 선택을 모두 완료 -> 종료
    # 그 중에 합이 0인 부분집합만 골라서 출력
    if idx == N:
        if sum(selected) == 0:
            cnt += 1
            print(*selected, cnt)
            return
    # 재귀호출
    # 2가지로 나뉨
    # idx번 원소를 부분집합에 포함하고 idx+1 단계로 이동
    subset(idx + 1, selected + [arr[idx]])
    # idx번 원소를 부분집합에 포함하지 않고 idx+1 단계로 이동
    subset(idx + 1, selected)

subset(0, [])
print(cnt)