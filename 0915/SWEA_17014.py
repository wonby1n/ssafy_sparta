# 자연수 N에 몇 번의 연산을 통해 다른 자연수 M을 만들려고 함.
# 사용할 수 있는 연산은 +1, -1, *2, -10
# 최소 몇 번의 연산을 거쳐야 하는가

from collections import deque


def bfs(N):
    q = deque()  # 큐 생성
    q.append((N, 0))  # 시작 숫자 N과 연산 횟수 0율 큐에 넣음

    while q:
        v, cnt = q.popleft()  # 현재 숫자와 지금까지 연산 횟수 꺼내기

        if v == M:  # 목표 숫자 M에 도달하면
            return cnt  # 지금까지 연산 횟수 반환

        # 가능한 연산 4가지
        for nv in (v + 1, v - 1, v * 2, v - 10):
            if 0 < nv <= 1000000 and not visited[nv]:  # M의 범위 내인지, 아직 방문하지 않았는지 확인
                visited[nv] = 1  # 방문 처리
                q.append((nv, cnt + 1))  # 큐에 다음 숫자와 연산 횟수 + 1 해서 넣기


T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())  # N : 처음 자연수, M : 만들고자 하는 자연수

    visited = [0] * 1000001  # 방문 여부 확인. N, M이 1 이상 1,000,000이라고 주어짐.
    visited[N] = 1  # 시작 숫자 방문 처리
    answer = bfs(N)  # BFS 함수 호출하여 최소 연산 횟수 구하기

    print(f'#{test_case} {answer}')