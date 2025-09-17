# 돌의 개수 N, 쓸 수 있는 최대 힘 K
N, K = map(int, input().split())
arr = list(map(int, input().split()))

power = []
# 한 번 이동하면 몇 번 움직일 수 있는지 확인용
for i in range(N):
    for j in range(i+1, N):
        a = (j - i) * (1 + abs(arr[i] - arr[j]))
        power.append(a)

        print(power)

visited = [0] * N

# 가장 왼쪽 돌에서 가장 오른쪽 돌로 이동할 수 있을지?
# 몇 번 반복해야 되는지 모르니 while문을 쓰자
# 마지막으로 이동한 곳
last = 0
# 이동한 횟수 (여기선 필요 없을 듯)
cnt = 0

while True:
    # 종료조건 : 만약 지금 내가 있는 곳이랑 마지막으로 이동한 곳이랑 같으면
    # 이동을 못하면 종료

    # 오른쪽으로 이동할 때 드는 power 알아내기
    for i in range(N):
        for j in range(i+1, N-1):
            power = (j - i) * (1 + abs(arr[i] - arr[j]))

            # 만약 내가 가진 힘이 power보다 크거나 같으면
            if K >= power:
                # 이동해버린다~
                last = arr[j]

