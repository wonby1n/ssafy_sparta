T = 1
for tc in range(1, T+1):
    t, N = map(int, input().split())
    arr = list(map(int, input().split()))

    graph = [[] for _ in range(100)]

    for i in range(N):
        a = arr[i*2]
        b = arr[i*2+1]
        graph[a].append(b)

    print(graph)


    visited = [0] * 100
    stack = []
    stack.append(0)
    visited[0] = 1
    answer = 0

    while stack:
        s = stack.pop()
        if s == 99:
            answer = 1
            break
        # 99가 아니라면 각 노드 방문
        for ns in graph[s]:
            if visited[ns] == 0:
                visited[ns] = 1
                stack.append(ns)

    print(f'#{tc} {answer}')