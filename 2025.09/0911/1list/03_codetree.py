# A : Y, 37 이상
# B : N, 37 이상
# C : Y, 36 이하
# D : N, 36 이하

count = [0] * 4

# 입력받기
arr = []
for _ in range(3):
    a, b = input().split()

    arr.append([a,int(b)])

for i in range(len(arr)):
    if arr[i][0] == 'Y':
        if arr[i][1] >= 37:
            count[0] += 1
        else:
            count[2] += 1
    else:
        if arr[i][1] >= 37:
            count[1] += 1
        else:
            count[3] += 1

result = ''

if count[0] >= 2:
    result = 'E'

print(*count, result)