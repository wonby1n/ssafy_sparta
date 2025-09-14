# 햄버거 재료 조합하기
def make_hamburger(cnt, num, num2):
    global result
    # 칼로리가 L보다 높아버리면 종료
    if num >= L:
        return
    # 기본적인 종료조건, n개 다 살펴봣으면 꺼지기
    if cnt == N:
        # 칼로리가 L보다 낮다면
        if num < L:
            result = max(result, num2)
        return

    make_hamburger(cnt+1, num + calo[cnt], num2 + score[cnt])
    make_hamburger(cnt + 1, num, num2)


T = int(input())
for tc in range(1, T+1):
    N, L = map(int, input().split())
    score = []
    calo = []
    # 입력받기
    for _ in range(N):
        a, b = map(int, input().split())
        score.append(a)
        calo.append(b)

    # 원하는 값
    # 제한 칼로리 이하의 조합 중에서 가장 맛에 대한 점수가 높은 애
    result = 0
    make_hamburger(0,0,0)

    print(f'#{tc} {result}')