# 1. 입력받기
arr = list(map(int, input().split()))

result = []
for x in arr:
    if x == 0:   # 0 나오면 거기서 멈춤
        break
    result.append(x)

N = len(result)

# 2. 10의자리 수 세기
b = []
for i in range(N):
    b.append(arr[i] // 10)

print(b)

# 3. count 배열 만들기
count = [0] * 10
for i in b:
    count[i] += 1

C = len(count)

for i in range(1, C):
    print(f'{i} - {count[i]}')