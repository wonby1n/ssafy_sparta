T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 열 인덱스의 순열(행 idx에는 열 p[idx]를 쓰겠다는 뜻)
    p = list(range(N))
    # list로 감싸는 게 안전하다고 함
    best = [float('inf')]

    def make_perm(idx, s):
        # 종료조건 1. 현재 합이 최
        if s >= best[0]:
            return

        # 종료조건
        if idx == N:
            if s < best:
                best[0] = s
            return

        # 현재 위치 idx에 놓일 열을 idx..n-1 중에서 하나씩 골라본다(순열 생성)
        for j in range(idx, N):
            # p[idx]와 p[j]를 교환해 열을 확정해 본다
            p[idx], p[j] = p[j], p[idx]
            # 교환해주고 이제 다음순번으로 넘어가기
            make_perm(idx+1, s + arr[idx][p[idx]])
            # 초기화시켜주기
            p[idx], p[j] = p[j], p[idx]

    make_perm(0,0)
    print(f'#{tc} {best[0]}')