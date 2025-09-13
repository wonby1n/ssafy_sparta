# 높이가 B이상인 탑 중에서 가장 높이가 낮은 탑
# 순서 상관 X, 순열 아님
# 개수 자유 , 조합 아님
# 부분집합 구하는 문제
def make_doby(cnt, doby_is_free):
    global max_doby
    # 가지치기, 지금까지 쌓은 탑이 이미 B 이상이면 더 볼 필요 없음
    if doby_is_free >= B:
        max_doby = min(doby_is_free, max_doby)
        return

    # 종료조건. 만약 사람 수만큼 다 세면
    if cnt == N:
        return

    # 재귀호출, 다음 애를 포함하는 거랑, 포함하지 않는 거
    make_doby(cnt + 1, doby_is_free + doby[cnt])
    make_doby(cnt + 1, doby_is_free)

T = int(input())
for tc in range(1, T+1):
    # N : 점원 수 # B : 점원들이 쌓을 탑
    N, B = map(int, input().split())
    doby = list(map(int, input().split()))

    # 구하고 싶은 거
    # 높이가 B 이상인 탑 중에서 가장 높이가 낮은 탑 - B
    max_doby = float('inf')

    # 함수 호출
    make_doby(0,0)

    print(f'#{tc} {max_doby-B}')