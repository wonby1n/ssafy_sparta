# 부분 집합

name = ['min', 'co', 'tim']

def recur(cnt, result):
    # 종료조건
    if cnt == 3:
        print(*result)
        return

    # 재귀호출 파트
    recur(cnt+1, result + [name[cnt]])
    recur(cnt +1, result)

recur(0,[])


# -------------------------

# 바이너리 카운팅

arr = [1, 2, 3, 4]
N = len(arr)

for i in range(1<<N):
    for idx in range(N):
        if i & (1<<idx):
            print(arr[idx], end = ' ')
    print()


# 5명 중 3명을 순서없이 고르기
arr = ['A', 'B', 'C', 'D', 'E']
N = 3
path = []

def recur(cnt, start):
    # N명을 뽑으면 종료
    if cnt == N:
        print(path)
        return

    for i in range(start, len(arr)):
        path.append(arr[i])
        recur(cnt+1, i+1)
        path.pop()

recur(0,0)