# 상자가 놓인 가로 칸의 수 N, 다음 줄에 각 칸의 상자 높이
N = int(input())
box = list(map(int, input().split()))

# 가장 큰 낙차를 저장할 변수 생성
result = 0

# 각 상자(i)를 기준으로 오른쪽 상자들과 낙차를 비교
for i in range(N):
    fall = 0    # 현재 상자(i)의 낙차를 저장할 변수
    # i번 상자의 오른쪽에 있는 상자들과 비교하여
    # 나보다 낮은 상자가 있을 때마다 낙차 1씩 증가
    for j in range(i, N-i): # 오른쪽 상자만 비교해야 하므로 j는 i+1부터 N까지
        if box[i] > box[j]: # 나보다 낮으면 낙차 가능
            fall += 1
    # 현재 상자(i)의 낙차가 지금까지의 최대값보다 크면 갱신
    if result < fall:
        result = fall

