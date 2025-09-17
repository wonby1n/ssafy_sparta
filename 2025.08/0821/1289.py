"""
시작은 0 * N
N이 4이고, 0100으로 가고 싶다면
2번째 꺼를 1로 설정 -> 0111
3번째 꺼를 0으로 설정 -> 0100
두번 하면 댐
"""
T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input()))
    N = len(arr)
    bit = [0] * N
    cnt = 0

    for i in range(N):
        if arr[i] != bit[i]:
            for j in range(i, N):
                bit[j] ^= 1
            cnt += 1

    print(f'#{tc} {cnt}')