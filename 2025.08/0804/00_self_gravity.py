# 상자가 놓인 가로 칸의 수 N
N = int(input())
box = list(map(int, input().split()))

# 내 오른쪽에 나보다 숫자가 작으면 낙차가 + 됨
# 최대 낙차 저장할 변수
total = 0

# 왼쪽부터 하나씩 확인하면서 낙차 계산
for i in range(N):
    fall = 0
    # 자신(i)의 오른쪽부터 N 전까지의 낙차 계산
    for j in range(i+1, N):
        # 만약 i번째(자신)이 j번째(다음꺼)보다 크다면, +1
        if box[i] > box[j]:
            fall += 1
        # 최대값 갱신
    if total < fall:
        total = fall

print(total)

# 일단 앞전 gravity문을 작성해보자
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    # 일단 총 합을 담을 변수를 만들자
    total = 0
    # 자기자신(i)보다 오른쪽 숫자가 작으면 낙차가 +1이 된다
    for i in range(N):
        # 반복문에서 값을 담을 변수를 만들자
        fall = 0
        # 자기자신(i)보다 오른쪽부터 N전까지
        for j in range(i+1, N):
            if arr[i] > arr[j]:
                fall += 0
        # if문에서 i+N까지 계산을 다 한 후 빠져나와서, 1번째 for문에서 fall이랑 total이랑 비교를 한다
        if total < fall:
            total = fall