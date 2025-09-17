# 낙차 출력 프로그램
# 가로 칸의 수 N, 다음 줄에 상자 높이
N = int(input())
box = list(map(int, input().split()))

# 오른쪽에 있는 상자들의 높이와 비교해서 높으면 낙차에 +1
# 초기값 세팅
total = 0
for i in range(N):
    fall = 0
    # 자기(i)의 오른쪽부터 N 전까지의 낙차 계산
    for j in range(i+1, N):
        if box[i] > box[j]:
            fall += 1
    if total < fall:
        total = fall