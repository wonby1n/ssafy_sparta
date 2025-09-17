T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())

    # 인접 리스트 생성
    graph = [[] for _ in range(V + 1)]

    # 간선 입력: 방향성 그래프이므로 한쪽만 연결
    for _ in range(E):
        s, e = map(int, input().split())
        graph[s].append(e)

    S, G = map(int, input().split())

    # 방문 배열
    visited = [0] * (V + 1)

    # ----- DFS (스택) 시작 -----
    stack = []                 # 무엇을 하는가: 다음에 방문할 노드를 담는 스택
    stack.append(S)            # 시작 노드 push
    visited[S] = 1             # 시작 노드 방문 표시

    found = 0                  # 무엇을 하는가: 경로 발견 여부(0/1)

    while stack:               # 무엇을 하는가: 스택이 빌 때까지 반복
        now = stack.pop()      # 무엇을 하는가: 현재 노드 하나 꺼내기

        if now == G:           # 무엇을 하는가: 도착 노드에 도달했는지 확인
            found = 1
            break              # 무엇을 하는가: 찾았으니 즉시 종료

        # 무엇을 하는가: 현재 노드에서 갈 수 있는 이웃 노드 확장
        for nxt in graph[now]:
            if visited[nxt] == 0:     # 무엇을 하는가: 아직 방문하지 않았으면
                visited[nxt] = 1      # 무엇을 하는가: 방문 표시
                stack.append(nxt)     # 무엇을 하는가: 다음 방문 후보로 추가

    print(f"#{tc} {found}")
