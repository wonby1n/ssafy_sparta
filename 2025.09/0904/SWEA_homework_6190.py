T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    max_danjo = -1

    # 리스트에 다 추가하지 말자.
    for i in range(N):
        for j in range(i+1, N):
            num = arr[i]*arr[j]
            s = str(num)
            n = len(s)
            found = True
            for k in range(n-1):
                if s[k] > s[k+1]:
                    found = False
                    break
                else:
                    continue
            if found:
                max_danjo = max(max_danjo, num)

    print(f'#{tc} {max_danjo}')

