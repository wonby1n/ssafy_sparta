def recur(idx, num):
    global result

    # 종료조건 : 만약 합이 k라면
    if num == K:
        result += 1
        return

    if idx == N:
        return

    recur(idx+1, num + arr[idx])
    recur(idx+1, num)

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))

    # 원하는 답
    result = 0

    # 함수 호출
    recur(0,0)
    print(f'#{tc} {result}')