outside = {'(':3, '*':2,'/':2,'-':1,'+':1}
inside = {'(':0, '*':2,'/':2,'-':1,'+':1}

arr = list(input().strip())

stack = []
answer = []


for token in arr:
    if token not in '()+-*/':
        answer.append(token)

    # 아니면
    else:
        # 만약 닫는 괄호라면
        if token == ')':
            # 스택이 있는동안 꺼낸다. ( 나올때까지
            while stack:
                s = stack.pop()
                if s == '(':
                    break
                stack.append(s)
        # 괄호가 아니라면
        # 안에 있는 게 밖에 있는 것보다 크거나 같으면 꺼내서 답에 추가
        # 아닐시 스택에 추가
        else:
            while stack and outside[token] <= inside[stack[-1]]:
                answer.append(stack.pop())
            stack.append(token)

# 혹시 스택에 먼가 남아있을까바
while stack:
    answer.append(stack.pop())