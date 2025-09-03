# 0에서 9까지 숫자가 적힌 N장의 카드
# 카드 장수 N, 카드 리스트

N = int(input())
arr = list(map(int, input().split()))

"""
카운팅 정렬이란, 숫자가 해당하는(똑같은) 인덱스 번호에 저장하고
누적합을 더하고, 뒤에서부터 차례로 정렬하는 것
"""
# 빈 리스트를 하나 만든다
num = [0] * 10 # 0에서 9까지라고 했으므로, 10개

# 반복문을 써서 내 원소를 리스트에 저장해보자
for i in arr:
    num[i] += 1

# 누적합을 더할 필요는 없음. 각 숫자카드가 몇 개인지 세서
# 구하고 싶은 값의 변수를 설정함
max_val = num[0]
max_sum = 0

for i in range(len(num)):
    if max_val < num[i]:
        max_val = num[i]
        max_sum = i
    elif max_val == num[i] and max_sum < i:
        max_sum = i

print(max_val, max_sum)