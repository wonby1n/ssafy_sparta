# 양팔 저울에 무게추 올리기
# 오른쪽이 늘 왼쪽보다 무게가 낮아야 함
# 오른쪽에 아무것도 안 올려도 됨
def recur(idx, left_sum, right_sum):
    global result
    # N개의 무게추를 다 올렸으면
    if idx == N:
        result += 1
        return

    # 1. 왼쪽 저울에 올리기
    recur(idx+1, left_sum + weight[idx], right_sum)

    # 2. 오른쪽 저울에 올리기 (단, 왼쪽보다 무거워지면 안 됨)
    if left_sum >= right_sum + weight[idx]:
        recur(idx+1, left_sum, right_sum + weight[idx])


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    weight = list(map(int, input().split()))

    # 원하는 값 : 양팔 저울에 모든 무게추를 올리는 방법
    result = 0

    # 오른쪽 왼쪽 배열 만들기
    right = [0] * N
    left = [0] * N

    # 함수 호출
    recur(0,0,0)
    print(f'#{tc} {result}')