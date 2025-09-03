from collections import deque

def bfs(v):
    q = deque()
    q.append(v)

    visited = [0] * (N+1)
    visited[v] = 1

    while q:
        sv = q.popleft()
        print(sv, end = ' ')
        for nv in graph[sv]:
            if visited[nv] == 0:
                visited[nv] = 1
                q.append(nv)

def dfs(v):
    stack = []
    visited = [0] * (N+1)

    stack.append(v)

    while stack:
        sv = stack.pop()
        if visited[sv]:
            continue
        visited[sv] = 1
        print(sv, end = ' ')
        for nv in reversed(graph[sv]):
            if visited[nv] == 0:
                stack.append(nv)

# 정점, 간선, 탐색 시장 정점
N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, N+1):
    graph[i].sort()

dfs(V)
print()
bfs(V)
print()