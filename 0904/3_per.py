path = [] # 뽑은 카드들을 저장
# N개의 카드 종류가 있는 경우 고를 수 있는 수만큼 만들어준다
# 0은 버린다
N = 6
used = [False] * (N+1)


def recur(cnt):
    if cnt == 3:
        print(*path)
        return

    for num in range(1,7): # 카드 1~6 중 하나를 선택
        if used[num]:
            continue

        used[num] = 1
        path.append(num) # 하나 선택했으니 다음 선택으로 이동
        recur(cnt + 1)
        path.pop()
        used[num] = 0

recur(0)