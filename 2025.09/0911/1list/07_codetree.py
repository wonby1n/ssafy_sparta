# N : A 원소 개수 M : B 원소 개수
# arr : A 원소
# brr : B 원소
N, M = map(int, input().split())
arr = list(map(int, input().split()))
brr = list(map(int, input().split()))

result = 'No'

for i in range(N-M+1):
    if arr[i:i+M] == brr:
        result = 'Yes'
        break
    else:
        continue

print(result)