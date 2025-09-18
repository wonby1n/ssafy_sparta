from collections import deque

def bfs(n, k):
    # q에 현재 좌표와 cnt 저장하기
    q = deque([(n,0)])
    visited = [0] * 100001
    visited[n] = 1

    while q:
        nq, cnt = q.popleft()

        # 만약 동생 위치에 도달하면
        if nq == k:
            return cnt

        for next_q in (nq*2, nq-1, nq+1):
            if 0 <= next_q <= 100000 and not visited[next_q]:
                visited[next_q] = 1
                q.append((next_q, cnt+1))


# 수빈이 위치, 동생 위치
N, K = map(int, input().split())

print(bfs(N, K))