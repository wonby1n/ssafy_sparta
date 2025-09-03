T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    # 최종 정답
    max_val = -1

    # 인덱스 0 부터 마지막까지 반복해서 돌기
    for i in range(N-1):
        # 그 다음 애들이랑 비교하기
        for j in range(i+1, N):
            # 만약 현재 좌표랑, 그 전 좌표랑 곱한 것이 단조라면?
            num = arr[i] * arr[j]
            n = str(num)
            M = len(n)
            danjo = True
            for k in range(1, M):
                # 만약 전꺼보다 작다면 단조 아님
                if n[k] < n[k-1]:
                    danjo = False
                    break
            if danjo and num > max_val:
                max_val = num

    print(f'#{tc} {max_val}')