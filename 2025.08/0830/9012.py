T = int(input())
for tc in range(1, T+1):
    arr = list(input().strip())

    stack = []
    answer = 'NO'

    # '(' 만나면 STACK에 넣는다.
    # ')' 만나면 stack에 원소가 있는지 확인하고, 안에 있는 원소를 뺀다
    for i in arr:
        if i == '(':
            stack.append(i)
        else:
            if stack:
                stack.pop()
                answer = 'YES'
            else:
                answer = 'NO'
                break
    if stack:
        answer = 'NO'
    
    print(answer)