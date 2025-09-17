N, M, K = map(int, input().split())
student = [int(input()) for _ in range(M)]

check = [0] * (N+1)
result = -1

for i in range(M):
    check[student[i]] += 1

for j in range(len(check)):
    if check[j] == K:
        result = j

print(check)