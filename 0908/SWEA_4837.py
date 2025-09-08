def recur(idx, result):
    global cnt
    # 종료조건 : idx가 끝까지 갔을 때
    if idx == len(A):
        # 원하는 원소 개수를 고르고, 원하는 합이라면
        if len(result) == N and sum(result) == K:
            cnt += 1
        return

    if len(result) > N or sum(result) > K:
        return

    recur(idx + 1, result + [A[idx]])
    recur(idx + 1, result)


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for tc in range(1, T + 1):
    N, K = map(int, input().split())

    # 1부터 12까의 숫자를 가진 집합 A
    A = [1,2,3,4,5,6,7,8,9,10,11,12]


    cnt = 0
    recur(0, [])
    print(f'#{tc} {cnt}')