outside = {'(':3, '/':2, '*':2, '-':1, '+':1}
inside = {'(':0, '/':2, '*':2, '-':1, '+':1}

N = int(input())
arr = list(input().strip())
# A, B, C, ... 순서로 N줄 값이 들어옴
vals = [int(input()) for _ in range(N)]

stack = []

for token in arr:
    # 만약 숫자라면 스택에 넣기
    if token not in '+-*/':
        idx = ord(token) - ord('A')
        stack.append(vals[idx])

    # 만약 연산자라면
    else:
        a = stack.pop()
        b = stack.pop()

        if token == '+':
            stack.append(b + a)
        elif token == '-':
            stack.append(b - a)
        elif token == '*':
            stack.append(b * a)
        elif token == '/':
            stack.append(b / a)

result = stack.pop()
print(f'{result:.2f}')