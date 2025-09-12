n, t = map(int, input().split())           # 격자 크기 n, 시간 t
r, c, d = input().split()                  # 초기 행, 열, 방향
r = int(r) -1
c = int(c) -1# 0-indexed로 변환
dir_map = {'R': 0, 'D': 1, 'L': 2, 'U': 3}
dir_num = dir_map[d]

# 시계 방향 기준: 동, 남, 서, 북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for _ in range(t):
    nr, nc = r + dx[dir_num], c + dy[dir_num]

    # 벽에 부딪히면 방향 전환
    if not (0 <= nr < n and 0 <= nc < n):
        dir_num = (dir_num + 2) % 4  # 반대 방향으로 전환
        continue  # 방향 전환만 하고 이동은 다음 초에

    # 정상 이동
    r, c = nr, nc

# 출력 (1-indexed로 다시 변환)
print(r + 1, c + 1)
