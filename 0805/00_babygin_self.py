# 0~9 사이의 숫자 카드
# run = 연속적인 번호 / triplet = 동일한 번호
# run과 triplet으로만 구성되면 baby-gin

num = int(input())
c = [0] * 12
# c[10], c[11]은 항상 0이며, run 확인을 위한 여분
# 6개가 입력되니까, 자릿수 모를 땐 while
for _ in range(6):
    # num % 10의 자리 알아내기
    c[num % 10] += 1
    # 알아냈으면 1의자리 제거 후 반복
    num //= 10

# 굳이 list를 안 쓰는 이유는 이게 더 효율이 좋다고 한다

# 카드 번호 0으로 설정
i = 0
# 구하고 싶은 triplet, run 둘 다 0으로 설정
tri = run = 0
# 카드는 9까지 있으므로,
while i < 10:
    if c[i] >= 3:
        c[i] -= 3
        tri += 1
        continue
    if c[i] >= 1 and c[i+1] >=1 and c[i+2]>=1:
        c[i] -= 1
        c[i+1] -= 1
        c[i+2] -= 1
        run += 1
        continue
    i += 1