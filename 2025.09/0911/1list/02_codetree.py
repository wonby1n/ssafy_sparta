# 입력받기
a = list(map(int, input().split()))
arr = []
for i in range(len(a)):
    if a[i] == 0:
        break
    arr.append(a[i])

# 1의 자리 수로 만들기
N = len(arr)
brr = []
for i in range(N):
    b = a[i]//10
    brr.append(b)


# count배열 만들기
count = [0] * 11

for i in brr:
    count[i] += 1

for i in range(len(count)-1, 0, -1):
    print(f'{(i)*10} - {count[i]}')