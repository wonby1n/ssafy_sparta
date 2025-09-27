N = int(input())
a1, b1, c1 = map(int, input().split())  # 첫 번째 자물쇠 비밀번호
a2, b2, c2 = map(int, input().split())  # 두 번째 자물쇠 비밀번호

def close(x, y):
    """
    두 수 x, y가 자물쇠 원형에서 '거리 2 이하'인지 확인하는 함수
    - abs(x-y) <= 2 : 일반적인 차이가 2 이하
    - (min(x,y) + N - max(x,y) <= 2) : 원형 고려 (예: N=6일 때 1과 6의 거리는 1)
    """
    return abs(x - y) <= 2 or (min(x, y) + N - max(x, y) <= 2)

def is_answer(i, j, k):
    """
    조합 (i, j, k)가 자물쇠를 열 수 있는지 확인
    - (a1, b1, c1)와 비교하여 세 자리 모두 거리 2 이하 → 열림
    - (a2, b2, c2)와 비교하여 세 자리 모두 거리 2 이하 → 열림
    """
    # 첫 번째 비밀번호와 비교
    if close(a1, i) and close(b1, j) and close(c1, k):
        return True
    # 두 번째 비밀번호와 비교
    if close(a2, i) and close(b2, j) and close(c2, k):
        return True
    return False

ans = 0
# 모든 조합 (i, j, k) 완전탐색
for i in range(1, N + 1):
    for j in range(1, N + 1):
        for k in range(1, N + 1):
            if is_answer(i, j, k):  # 열 수 있으면 개수 증가
                ans += 1

print(ans)
