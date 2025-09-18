n = int(input())
A = [0] + list(map(int, input().split()))

# 최솟값을 원하므로 값을 무한대로 설정
result = float('inf')

# 반복문 시작, 리스트 받을 때 1번부터 시작되게 받았으므로 1번부터 반복하게 설정해둠
for i in range(1,n+1):
    walk = 0
    for j in range(1,n+1):
        walk += A[j] * abs(i-j)

    result = min(walk, result)

print(result)