N = int(input())
a,b,c = map(int, input().split())

# 1부터 N까지 숫자를 뽑아서 조합하기

def found(N,a,b,c):
    cnt = 0
    # 백의 자리 탐색
    for i in range(1,N+1):
        # 십의 자리 탐색
        for j in range(1,N+1):
            # 일의 자리 탐색
            for k in range(1,N+1):
                # 한 자리라도 차이가 2 이내이면
                if abs(a-i) <= 2 or abs(b-j) <= 2 or abs(c-k)<= 2:
                    cnt += 1

    return cnt

result=found(N,a,b,c)
print(result)
