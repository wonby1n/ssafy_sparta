# 부분수열 중 원소를 다 더한 값이 S가 되는 경우
def recur(idx, num, cnt):
    global result
    # 만약 N개를 다 살펴본다면 종료
    if idx == N:
        if num == S and cnt > 0:  # 공집합 제외
            result += 1
        return

    recur(idx + 1, num + arr[idx], cnt+1)
    recur(idx + 1, num, cnt)

# N : 정수의 개수 S : 정수
N, S = map(int, input().split())
arr = list(map(int, input().split()))

# 원하는 최종 값. 값이 S가 되는 경우의 수
result = 0

recur(0,0,0)
print(result)