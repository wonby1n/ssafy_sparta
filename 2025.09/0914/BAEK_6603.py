def make_lotto(cnt, lotto):
    # 종료조건 : 6개 다 고르면 출력
    if len(lotto) == 6:
        print(*lotto)
        return

    # 뽑을 게 없으면 종료
    if cnt == K:
        return

    make_lotto(cnt+1, lotto + [lotto_list[cnt]])
    make_lotto(cnt+1, lotto)

while True:
    line = input().split()
    if line[0] == '0':
        break
    K = int(line[0])
    lotto_list = list(map(int, line[1:]))

    make_lotto(0,[])
    print()