arr = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 1, 1, 0],
    [0, 0, 0, 2, 0],
]


N = 5
start_r, start_c = -1, -1

for r in range(N):
    for c in range(N):
        if arr[r][c] == 2:
            start_r, start_c = r,c

r, c = start_r, start_c # 출발점 찾기

while r > 0: # r이 0일때까지 (r에 -1 해주므로, r==1이상은 되어야 위로 갈 수 있음)
    # 위로 올라가기 전에 좌우부터 체크
    while arr[r][c-1] == 1: # 만약에 왼쪽에 1이 있다면 (if일때는 1칸만 갔음, while이면 반복해서 간다.)
        c -= 1 # 왼쪽으로 간다
        arr[r][c] = 3

    r -= 1 # 위로 올라간다
    arr[r][c] = 3

for i in range(N):
    print(arr[i])