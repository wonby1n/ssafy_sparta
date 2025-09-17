# 1
# 상,하,좌,우
di = [-1,1,0,0] # 행
dj = [0,0,-1,1] # 열

for k in range(4): # 4방향일 때, 숫자는 고정
    ni = i + di[k] # ni : 새로운 좌표, i는 현재 행 좌표, di[k] : di에서 k번째에 위치하는 원소
    nj = j + dj[k] # nj : 새로운 좌표, j는 현재 열 좌표, dj[k] : dj에서 k번째에 위치하는 원소
    if 0 <= ni < n and 0 <= nj < m # 범위 안쪽
        print(arr[ni][nj])

# 2
for i in range(N):
    for j in range(M):
        # dj di를 for문 안에서 정의
        for di, dj in [[-1,0],[1,0],[0,-1],[0,1]]: #리스트 차례대로 상,하,좌,우
            ni = i + di
            nj = j + dj
            if 0 <= ni < n and 0 <= nj < m:
                print(arr[ni][nj])