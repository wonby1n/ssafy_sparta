T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))

    # 원하는 값
    answer = 0

    for i in range(N):
        # 차이 별로 안나는 애들이면 넣어주기
        giants = 0
        for j in range(i+1, N):
            if abs(arr[i] - arr[j]) <= K:
                giants += 1
