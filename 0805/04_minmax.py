# N개의 양의 정수
# N개의 양수 리스트

N = int(input())
nums = list(map(int, input().split()))

# 구하고 싶은 큰 값이랑 작은 값 변수 정해주기
max_val = nums[0]
min_val = nums[0]
max_i = 0
min_i = 0

# 큰 값은 마지막에 있는 걸 출력해야 하니까 같거나를 추가
for i in range(len(nums)):
    if max_val <= nums[i]:
        max_val = nums[i]
        max_i = i

# 작은 값은 맨 처음에 있는 걸 출력해야 하니까 처음부터 확인
for i in range(len(nums)):
    if min_val > nums[i]:
        min_val = nums[i]
        min_i = i

result = abs(max_i-min_i)

print(f'#{test_case} {result}')