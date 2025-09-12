arr = input()
N = len(arr)

cnt = 0

for i in range(N):
    if arr[i] == '(':
        for j in range(i+1, N):
            if arr[j] ==')':
                cnt +=1

print(cnt)