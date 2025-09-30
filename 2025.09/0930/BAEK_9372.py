# 상근이가 모든 나라를 여행하려고 할 때, 필요한 비행기의 최소 개수를 구해라
# 나라가 N개, 나라들을 전부 연결하려면 최소한 N-1개의 노선만 있으면 됨
# 트리구조

T = int(input())
# 국가의 수 N, 비행기의 종류 M
for tc in range(1, T+1):
    N, M = map(int, input().split())
    for _ in range(M):
        a, b = map(int, input().split())
    print(N-1)