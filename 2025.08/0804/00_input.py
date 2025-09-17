# 입력으로 숫자 하나가 들어온다
# 6
N = int(input())
print(N)

# 입력으로 숫자 여러개가 들어오는데, 공백으로 구분이 되어있다
# 1 2 3 4 5
lst = list(map(int, input().split()))
print(lst)

# 입력으로 숫자 여러개가 들어오는데, 공백으로 구분이 안되어 있다
# 12345
lst = list(map(int, input()))
print(lst)