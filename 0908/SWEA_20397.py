T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for tc in range(1, T + 1):
    # N : 돌의 수 M: 뒤집기 횟수
    N, M = map(int, input().split())

    arr = list(map(int, input().split()))

    # i : 번째부터 j : 개의 돌을 뒤집음
    for _ in range(M):
        i, j = map(int, input().split())


