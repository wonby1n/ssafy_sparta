T = 10
for tc in range(1, T+1):
    N, arr = input().split()

    stack = []

    for i in arr:
        # 스택이 있고 맨 마지막 stack이랑 지금 넣을 원소랑 같다면
        if len(stack) >0 and stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)