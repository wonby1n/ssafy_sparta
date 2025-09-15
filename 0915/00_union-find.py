N = 10

p = [0] * (N+1)

# 초기화 연산
# x 자기 자신이 대표인 집합을 만든다
def make_set(x):
    p[x] = x

# x가 속한 집합의 대표가 누구니?
def find_set(x):
    if p[x] != x:
        return x
    return find_set(p[x])


# 경로 압축 버전
# 모든 x에 대해서 find_set2(x)를 한번씩 호출이 되어야 경로 압축이 일어난다
def find_set2(x):
    if p[x] != x:
        p[x] = find_set2(p[x])


# x가 속한 집합과 y가 속한 집합을 합치는 연산
def union(x,y):
    # x가 속한 집합의 대표를 구함
    king_x = find_set2(x)
    king_y = find_set2(y)
    # y가 속한 집합의 대표를 구함

    # 두 집합의 대표가 같으면
    if king_x == king_y:
        return

    # 다르면, 더 작은쪽이나 x를 대표로
    p[king_y] = king_x

# 랭크를 사용한 집합의 높이 구별
# 랭크가 작은 집합을 랭크가 큰 집합에 합친다
rank = [0] * (N+1)

def union2(x,y):
    king_x = find_set2(x)
    king_y = find_set2(y)

    # 합칠때 두 집합의 랭크를 비교해서 더 큰 쪽을 대표로 삼겠다
    