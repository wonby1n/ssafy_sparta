N = int(input())
arr = list(map(int, input()))

# 카운팅 정렬은 섞여있는 정수의 리스트를 하나씩 꺼내 해당하는
# 인덱스에 해당하는 숫자들을 넣고, 누적합을 구하고 정렬하는 것

# 일단 빈 리스트를 만든다.
list = [0] * (N+1)

# 리스트에 있는 정수를 하나씩 꺼내 해당하는 인덱스 리스트에 저장
for i in arr:
    list[i] += 1

# 누적합 구하기.내 앞 원소의 총 개수와 내 원소의 개수를
# 더하는 것이 누적합
for i in range(1, N+1):
    list[i] += list[i-1]

# 정렬하기. 마지막부터 정렬
# 맨 뒤에 있는 숫자에 해당 위치를 선정해준다
# len(list)-1 이 마지막 인덱스라는 뜻이라네요
for i in range(len(arr)-1, -1, -1):
    x = arr[i]
    list[x] -= 1
    output[list[x]] = x

print(output)