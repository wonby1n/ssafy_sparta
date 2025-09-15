'''
7 8
1 2
1 3
2 4
2 5
4 6
5 6
6 7
3 7

또는

7 8
0 1 1 0 0 0 0
1 0 0 1 1 0 0
1 0 0 0 0 0 1
...
인접 행렬로 들어오는 경우도 있음

'''
V, E = map(int, input().split())

# 인접 행렬 (0,1 로 연결 유무를 모두 저장)
# 7 * 7 의 0배열 (1~7 정점 번호를 활용)
graph = [[0] * (V + 1) for _ in range(V + 1)]
for _ in range(E):
    start, end = map(int, input().split())
    graph[start][end] = 1
    graph[end][start] = 1 # [주의!] 양방향이면 여기까지 적기


# 인접 리스트 (연결된 간선만 저장)
graph = [[] * (V + 1) for _ in range(V + 1)]
for _ in range(E):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start) # 양방향인 경우

