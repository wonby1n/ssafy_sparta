# 정사각형 안 정사각형이 얼마나 들어가는지 확인하기
# 일단 큰 정사각형 만들기
T = int(input())

for tc in range(1, T+1):
    # N : 큰 정사각형의 크기
    # M : 작은 정사각형의 크기
    N, M = map(int, input().split())
    paper = [[0] * N for _ in range(N)]

    # 종이에 찍을 스탬프 번호
    stamp = 1

    # 큰 정사각형의 모든 위치에서 작은 정사각형 만들기 시작
    # 작은 정사각형을 만들기 시작할 수 있는 위치를 예상 가능
    # 큰 정사각형의 마지막 인덱스 N-1
    # (N-1,N-1)에서 작은 정사각형을 만들기 시작하면
    # 작은 정사각형은 (N,N) 이런 위치를 포함하게 된다.
    # 큰 정사각형에서는 이 위치가 접근 불가능한 인덱스(범위를 벗어남)

    # 미리 시작 위치를 작은 정사각형의 크기만큼 뺀 상태에서 순회
    for i in range(N - M + 1):
        for j in range(N - M + 1):
             for k in range(M):
                for l in range(M):
                    paper[i+k][j+l] = stamp
                stamp += 1

    print(f'#{tc}')
    for page in paper:
        print(*page)