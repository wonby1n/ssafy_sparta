T = int(input())
for tc in range(1, T+1):
    arr = list(input().split())

    # 넣을 스택
    stack = []
    # 결과
    answer = 'error'

    for s in arr:
        if s not in '+-*/.':
            stack.append(int(s))
        elif s in '+-*/':
            if len(stack) < 2:
                break
            a = stack.pop()
            b = stack.pop()
            if s == '+':
                stack.append(a + b)
            elif s == '-':
                stack.append(b - a)
            elif s == '/':
                if a == 0:
                    break
                stack.append(b // a)
            elif s == '*':
                stack.append(a * b)
        elif s == '.':
            if len(stack) == 1:
                answer = stack.pop()
                break
        else:
            break

    print(f'#{tc} {answer}')