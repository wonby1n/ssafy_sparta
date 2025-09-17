T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for tc in range(1, T + 1):
    # N : 돌 개수 M : 몇 번 뒤집는지
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    stone = []

    # i : 번째부터 j : 개의 돌을 뒤집음
    for _ in range(M):
        i, j = map(int, input().split())

        # 색은 i-1번째로 지정
        color = arr[i-1]

        # i-1번째부터 i-1+j번째까지의 돌을 반복문 돌린다
        for c in range(i-1, i-1+j):
            # 범위 안에 있으면 색 변경
            if 0 <= c < N:
                arr[c] = color

    print(f'#{tc}', *arr)