arr = list(map(int, input().split()))

result = float('inf')
N = len(arr)
total = sum(arr)
half = N//2

def pick(start, picked, lst):
    global result

    # 종료조건
    if picked == half:
        one = sum(lst)
        two = total - one
        diff = abs(one-two)
        # 최소값 갱신
        if diff < result:
            result = diff
        return

    for i in range(start, N):
        lst.append(arr[i])
        pick(i+1,picked+1,lst)
        lst.pop()


pick(0,0,[])
print(result)
