n = int(input())
nums = list(map(int, input().split()))

cnt = [0] * 1000
max_cnt = -1

for i in range(n):
    cnt[nums[i]] += 1

for j in cnt:
    if cnt[j] == 1:
        max_cnt = j

print(max_cnt)