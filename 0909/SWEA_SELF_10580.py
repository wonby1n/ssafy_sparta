# 전봇대끼리 교차하는 경우
# 1. A전봇대의 시작점이 B전봇대의 시작점보다 높고,
#    A전봇대의 끝점이 B전봇대의 끝점보다 낮으면
# 2. A전봇대의 시작점이 B전봇대의 시작점보다 낮고
#    A전봇대의 끝점이 B전봇대의 시작점보다 높으면

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    arr = []
    cnt = 0

    # 입력받으면서 비교하기
    for _ in range(N):
        start, end = map(int, input().split())

        for now_start, now_end in arr:
            if start > now_start and end < now_end:
                cnt += 1
            if start < now_start and end > now_end:
                cnt += 1

        arr.append([start,end])

print(cnt)