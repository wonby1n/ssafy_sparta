N = 5
A = [1,2,3,4,5]

# 찾고자 하는 값
key = 4

# 반복문을 통해 key가 있는지 검사
for i in range(N):
    if A[i] == key:
        print('찾았다', i)
        break

else:
    print('없음')

# 재귀함수를 통해서 key가 있는지 검사
def search(idx, key):
    found = False
    # 종료
    # 5번 다 돌면 종료
    if idx >= N and not found:
        print('없음')
        return
    # 재귀호출
    if A[idx] != key:
        search(idx + 1, key)
    else:
        print('찾았다', idx)
        return

search(0, key)
print()