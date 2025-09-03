# 0~9 사이의 숫자 카드 중 임의의 카드 6장
# 3장의 카드가 연속 = run
# 3장의 카드가 연속 = triplet
# 6자리의 숫자를 입력받음

T = int(input())

for tc in T(1, T+1):
    num = int(input())

    # c[10], c[11]은 항상 0이며, run 확인을 위한 여분
    count = [0] * 12

    # num을 하나씩 쪼개서 count에 저장
    for i in range(6): # 카드가 6장이니까 6번 반복
        count[num % 10] += 1 # 맨 끝(1의 자리) 숫자 카드 개수 +1
        num //= 10 # 이미 센 1의 자리 제거

    # 카드 인덱스를 0으로 설정해 줌
    i = 0

    # 원하는 값의 초기값도 설정
    run = tri = 0

    while i < 10: # 카드 번호 0~9까지만 확인
        # triplet 확인: 같은 숫자 카드가 3장 이상 있는 경우
        if count[i] >= 3:
            count[i] -= 3
            tri += 1
            continue
        if count[i] >= 1 and count[i+1] >=1 and count[i+2] >=1:
            count[i] -= 1
            count[i+1] -= 1
            count[i+2] -= 1
            run += 1
            continue
        i += 1  # run/triplet이 없으면 다음 숫자 검사

    if tri + run == 2:
        print('Baby Gin')
    else:
        print('Lose')