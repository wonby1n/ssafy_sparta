T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    n_arr = list(map(int, input().split()))
    m_arr = list(map(int, input().split()))

    # N이랑 M 숫자가 뒤죽박죽으로 나와서, 숫자 고정
    if N < M:
        N,M = M, N
        n_arr, m_arr = m_arr, n_arr

    # 구하고 싶은 값
    result = 0

    # M 길이만큼 N 안에서 돌기
    for i in range(N-M+1):
        now_val = 0
        # 그 안에서 M만큼 보기
        for j in range(M):
            now_val += n_arr[i+j] * m_arr[j]

        result = max(now_val, result)


    print(f'#{tc} {result}')
