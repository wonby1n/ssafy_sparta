T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    for _ in range(M):
        i, j = map(int, input().split())
        i -= 1

        # j개의 쌍을 비교해야 하므로 자기 자신 제외(1부터 시작)로 범위 잡아야 함
        for k in range(1, j+1):
            left = i - k
            right = i + k

            # 범위를 벗어나면 뒤집기 자체를 멈춤
            if left < 0 or right >= N:
                break

            # 같은 색이면 뒤집고, 다른 색이면 가만히 둔다
            if arr[left] == arr[right]:
                arr[left] ^= 1
                arr[right] ^= 1


    print(f'#{tc}', *arr)