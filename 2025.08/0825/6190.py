T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    max_danjo = -1  # 단조 증가하는 수가 없을 경우 -1을 출력하기 위해

    # 모든 두 수의 쌍을 곱하여 확인
    for i in range(N):
        for j in range(i + 1, N):
            num = arr[i] * arr[j]

            s = str(num)
            ok = True
            for k in range(len(s) - 1):
                # 현재 자릿수가 다음 자릿수보다 크면 단조 증가가 아님
                if int(s[k]) > int(s[k + 1]):
                    ok = False
                    break
            if num > max_danjo:
                max_danjo = num

    print(f'#{tc} {max_danjo}')