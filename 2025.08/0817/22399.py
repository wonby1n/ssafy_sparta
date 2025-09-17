T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    # 소 / 중 / 대 이렇게 세개로 나눠야 함
    s = []
    m = []
    l = []

    answer = -1

    # 1, 2, 3이 들어왔으면 소, 중, 대 이렇게 세개로 나눠줄 수 있음
    # 어떤 기준으로 나누게 해야 할까
    # 여기선 숫자가 차이나서 하나씩 나눠주는 게 되지만
    # 111 3 이렇게 들어오면 소, 대 로만 나눠야 해서 답이 없음

    for carrot in arr:
        if carrot