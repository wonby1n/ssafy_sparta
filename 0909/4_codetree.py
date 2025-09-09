offset = 100
check = [0] * 201

n = int(input())
for _ in range(n):
    a, b = map(int, input().split())

    a += offset
    b += offset

    if a > b:
        a, b = b, a

    for i in range(a,b):
        check[i] += 1

print(max(check))