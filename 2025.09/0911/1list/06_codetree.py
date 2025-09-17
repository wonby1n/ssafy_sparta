# 1 a : a번째 원소 출력
# 2 b : b원소를 찾아, 인덱스 출력 (여러개일시, 제일 처음 idx), 없으면 0
# 3 s e : s번째부터 e번째까지 각 원소의 값을 차례대로 출력

N, Q = map(int, input().split())
arr = list(map(int, input().split()))
for _ in range(Q):
    a, *b = map(int, input().split())

    if a == 1:
        print(arr[b[0]-1])

    elif a == 2:
        found = 0
        for i in range(N):
            if arr[i] == b[0]:
                found += i+1
                break
        print(found)

    elif a == 3:
        s, e = b
        result = []
        for i in range(s-1, e):
            result.append(arr[i])
        print(*result)