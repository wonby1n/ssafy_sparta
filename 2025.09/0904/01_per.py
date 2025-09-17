N = 5

A = [1,2,3,4,5]
B = [0] * N
# 반복문을 통해서 A배열을 B에 복사
for i in range(N):
    B[i] = A[i]

print(B)



A = [1,2,3,4,5]
B = [0] * N
# 재귀를 통해서 A배열을 B에 복사
def mycopy(cnt):
    # 종료
    if cnt >= 5:
        return
    # 재귀호출 (다음단계)
    # 재귀호출을 하기 전에 현재 단계에서 수행해야 할 작업을 하고 넘어간다.
    B[cnt] = A[cnt]
    mycopy(cnt+1)

mycopy(0)
print(B)