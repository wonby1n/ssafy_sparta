def recur(idx, now_height):
    global min_val
    # 가지치기 : 만약 지금까지 구한 높이가 B이상이 되면 조건 충족
    # 그러니까 더 쌓지 말고 return
    if now_height >= B:
        min_val = min(now_height, idx)
        return
    # 종료조건 : 만약 점원 N명을 다 고려했다면 종료
    if idx == N:
        return

    # 재귀호출
    # 점원 한명씩 고려할때마다 cnt+1 해주기, 현재까지 키 합에 현재 점원 키 더해주기
    recur(idx+1, now_height + people[idx])
    # 현재 점원 포함 안하는 버전
    recur(idx+1, now_height)


T = int(input())
for tc in range(1, T+1):
    # N : 점원들 수 B : 탑의 높이
    N, B = map(int, input().split())
    # 점원들 키
    people = list(map(int, input().split()))
    # 원하는 값 : (높이가 B 이상인, 높이가 가장 낮은 탑) - B
    min_val = float('inf')