T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = list(input().strip())

    outside = {'(':3, '/':2, '*':2, '-':1, '+':1}
    inside = {'(':3, '/':2, '*':2, '-':1, '+':1}

    stack = []
    answer = []

    for token in arr:
        if token not in '+-*/':
            answer.append(token)

        else:
            while stack and outside[token] <= inside[stack[-1]]:
                answer.append(stack.pop())
            stack.append(token)

    while stack:
        answer.append(stack.pop())

    stack2 = []

    # 계산식. 간단하다
    for tok in answer:
        if tok not in '+-*/':
            stack2.append(tok)

        else:
            a = int(stack2.pop())
            b = int(stack2.pop())
            if tok == '+':
                stack2.append(b+a)
            elif tok == '*':
                stack2.append(b*a)

    result = stack2.pop()
    print(f'#{tc} {result}')