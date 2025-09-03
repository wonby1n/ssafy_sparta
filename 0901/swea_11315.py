T = int(input())
for tc in range(1, T+1):
    N =int(input())
    arr = [list(input().strip()) for _ in range(N)]

    # 답
    result = 'NO'
    # 델타
    delta = [[-1,0],[1,0],[0,-1],[0,1]]
    delta2 = [[1,1],[-1,-1],[1,-1],[-1,1]]

    for r in range(N):
        for c in range(N):
            if arr[r][c] == 'o':

                for dr, dc in delta:
                    black = 1
                    for step in range(1,N):
                        nr = r + dr * step
                        nc = c + dc * step
                        if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] != '.':
                            black += 1
                        if black >= 5:
                            result = 'YES'
                        else:
                            break
    
                for dr, dc in delta2:
                    black = 1
                    for step in range(1,N):
                        nr = r + dr * step
                        nc = c + dc * step
                        if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] != '.':
                            black += 1
                        if black == 5:
                            result = 'YES'
                        else:
                            break

print(result)