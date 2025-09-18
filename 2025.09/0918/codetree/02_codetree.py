# 들어오는 문자들을 리스트로 받아준다
A = list(input().strip())
n = len(A)

# 원하는 답
cnt = 0

# 반복문을 돌면서 '('를 만나면
for i in range(n):
    if A[i] == '(':
        # 그 다음꺼랑 비교하면서 괄호가 닫히면 cnt에 1 추가
        for j in range(i+1, n):
            if A[j] == ')':
                cnt += 1

print(cnt)