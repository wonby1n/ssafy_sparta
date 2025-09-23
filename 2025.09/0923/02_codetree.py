n, k = map(int, input().split())
x = []
c = []
for _ in range(n):
    pos, char = input().split()
    x.append(int(pos))
    c.append(char)

arr = [0] * 101

# G = 1점, H = 2점
for i in range(n):
    if c[i] == 'G':
        arr[x[i]] += 1
    else:
        arr[x[i]] += 2

result = 0

# 길이가 k인 구간 → start ~ start+k (끝 포함!)
for start in range(0, 101 - k):
    cnt = 0
    for idx in range(start, start + k + 1):  # k+1개
        cnt += arr[idx]
    result = max(result, cnt)

print(result)
