def make_bag(cnt, bag, val):
    global max_val
    # 가지치기, 만약 버틸 수 있는 무게보다 커진다면
    if bag > K:
        return

    # 종료조건. 물건을 다 봤으면
    if cnt == N:
        max_val = max(val, max_val)
        return

    make_bag(cnt+1, bag + weight[cnt], val+value[cnt])
    make_bag(cnt + 1, bag, val)

N, K = map(int, input().split())
weight = []
value = []

# 물건의 무게랑 가치를 다르게 입력받기
for _ in range(N):
    a, b = map(int, input().split())
    weight.append(a)
    value.append(b)

# 원하는 값: 가치의 최댓값
max_val = 0

# 함수 호출
make_bag(0,0,0)
print(max_val)