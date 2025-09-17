T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 첫 번째 전봇대 높이 A 기준으로 오름차순 정렬
    arr.sort()

    cnt = 0
    # B에서의 역순쌍 개수를 센다 => 교차 개수와 동일
    for i in range(N):
        # i 뒤의 원소들과 비교해 B[i] > B[j]면 교차 1 추가
        for j in range(i + 1, N):
            if arr[i][1] > arr[j][1]:
                cnt += 1

    print(f'#{tc} {cnt}')