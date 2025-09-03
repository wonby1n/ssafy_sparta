N = int(input)
arr = list(map(int, input()))

def counting_sort(data, temp, n):
    # 일단 빈 리스트를 만들어준다
    count = [0] * (k+1)

    # 원소들을 하나씩 빼서 세준다
    for i in arr:
        count[i] += 1

    # 누적합 구하기
    for i in range(1, k+1):
        count[i] += count[i-1]

    # 마지막부터 시작해서 자리로 보내기
    for i in range(len(arr)-1, -1, -1):
        x = arr[i]
        count[x] -= 1
        temp(count[x]) = arr[x]

nums = [0,4,1,3,1,2,4,1] # 정렬 대상 배열
result = [0] * len(nums) # 정렬 결과

counting_sort(nums,result, max(nums))
print(result)