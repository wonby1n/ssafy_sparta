"""
N M K = 2 2 2
N -> 2명의 사람
M -> 2초에
K -> 2개 만들 수 있음
N개의 정수 3 4

2초에 2개
2명한테 줄 수 있음
"""
T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    people = list(map(int, input().split()))
    people.sort()

    answer = ''

    # 붕어빵 만들기
    for i in range(N):
        time = people[i]
        bung = (time // M) * K
        customer = i + 1

    if customer > bung:
        answer = 'Possible'
    else:
        answer = 'Impossible'

    print(f'#{tc} {answer}')