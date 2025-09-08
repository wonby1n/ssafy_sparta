N = int(input())
arr = list(map(int, input().split()))

# 일단 구하고 싶은 jump 수
jump = 0
# 내가 지금 있는 좌표?
now = 0
# 그리고 움직일 idx
idx = 0

# 가장 왼쪽 끝에서 오른쪽 끝으로 가려고 한다
# 칸에 적혀 있는 수만큼 점프할 수 있다

# 몇 번 움직여야 되는지 모르므로 while을 쓴다
while True:
    # 종료조건 1. 만약 현재 인덱스가 N이면 종료
    if idx >= (N-1):
        break

    # 0번부터 시작, arr[idx]로 이동한다
    now = arr[idx]
    idx += now
    jump += 1

    # idx가 범위를 넘으면
    if idx >= N-1:
        break

    # 0을 만나면 되돌아간다
    if arr[idx] == 0:
        arr[idx] = arr[idx-1]
        jump += 1

    # 근데 최소 움직이는 수를 알고 싶으니까, 일단 최대로 가보고 전 인덱스가 내보다 크면
    # 그쪽으로 가는 게 낫지 않을까..

print(jump)