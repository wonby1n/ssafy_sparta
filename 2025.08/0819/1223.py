icp = {'(':3, '*': 2, '/':2, '+': 1, '-':1}
isp = {'(':0, '*': 2, '/':2, '+': 1, '-':1} # 스택안

T = 10
for tc in range(1, T+1):
    N = int(input())
    infix = input()

    stack = []
    postfix = ''

    for token in infix:
        # 만약에 연산자면
        if token in '+*':
            # 스택이 비어있거나, top(마지막 저장원소)의 우선순위가 높으면
            if not stack or isp[stack[-1]] < icp[token]:
                stack.append(token)
            else: # 아니면
                # 스택이 차있거나 top의 우선순위보다 같거나 작으면
                # 스택이 비거나, top의 우선순위가 낮을 때 까지 pop
                while stack and isp[stack[-1]] >= icp[token]:
                    postfix += stack.pop()
                stack.append(token)
        else: # 만약에 숫자면
            postfix += token
    while stack:
        postfix += stack.pop() # 남은 연산자 pop

    # postfix 연산
    for x in postfix:
        if x in '+*': # 연산자인 경우
            right = stack.pop() # 오른쪽 피연산자
            left = stack.pop() # 왼쪽 피연산자
            c = 0
            if x == '*':
                c = left * right
            elif x == '+':
                c = left + right
            stack.append(c)
        else: # 피연산자인 경우
            stack.append(int(x))

    print(f'#{tc} {stack.pop()}')