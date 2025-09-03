# N개의 0과 1로 이루어진 수열
# 연속한 1의 개수 중 최대값을 출력
# N = 수열의 길이
# 리스트가 공백 없이 제공

N = int(input())
nums = list(map(int, input()))

# 찾고 싶은 값의 변수 지정
count = 0
max_count = 0

# 연속하는 1의 개수 중에서 최대값을 출력해야 함
# 내 옆에 있는 원소가 1인지 알아야 하고, 1이면 +해줘야 함
# 만약 0이면 새로운 반복 시작
# count 끼리 비교해서 더 긴 count를 출력해야 함 -> 새로운 count 변수 만들어야 함
for i in range(N):
    if nums[i] == 1:
        count += 1
        if count > max_count:
            max_count = count
    else:
        count = 0

print(max_count)
