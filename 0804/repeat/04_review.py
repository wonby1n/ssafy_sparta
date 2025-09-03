# N개 건물, 건물의 높이
N = int(input())
tower = list(map(int, input().split()))

# 내 양 옆 건물(2개)간의 차이를 구하는 것
# 맨 끝 2자리까지는 0이니까 차이를 구할 필요 없음
# 구하고 싶은 값을 초기값 설정
sun_light = 0

# 양쪽 두 칸을 기준으로 조망을 계산하므로
# 시작 인덱스는 2, 끝 인덱스는 N-2 직전까지 (인덱스 기준)
for i in range(2, N-2):
my_tower = tower[i]

# 내 양 옆의 건물들을 저장해준다
left1 = tower[i-1]
left2 = tower[i-2]
right1 = tower[i+1]
right2 = tower[i+2]

# 제일 큰 빌딩 값을 임의로 지정해줌
max_tower = left1
if max_tower < left2:
    max_tower = left2
if max_tower < right2:
    max_tower = right2
if max_tower < right1:
    max_tower < right1

if my_tower > max_tower:
    sun_light = my_tower - max_tower

# 현재 건물이 가장 높은 건물보다 높을 경우에만 조망권 확보 가능
# 확보 가능한 세대 수는 (현재 건물 높이 - 주변 최고 높이)