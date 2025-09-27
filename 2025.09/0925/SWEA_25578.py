# T = int(input())
# for tc in range(1, T+1):

N, M = map(int, input().split())

big_grid = [list(map(int, input().split())) for _ in range(N)]
small_grid = [list(map(int, input().split())) for _ in range(M)]

for r in range(N-M+1):
    for c in range(M):
