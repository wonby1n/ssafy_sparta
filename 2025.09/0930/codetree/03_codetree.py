X, Y = map(int, input().split())

def is_interesting(num):
    s = str(num)
    n = len(s)
    
    # 각 자리 빈도 세기
    freq = {}
    for ch in s:
        if ch not in freq:
            freq[ch] = 0
        freq[ch] += 1

    # 조건1: 전부 같은 숫자 x
    if len(freq) == 1:
        return False
    
    # 조건2: 정확히 두 종류 숫자만 존재해야 함
    if len(freq) == 2:
        values = list(freq.values())
        # 하나는 (n-1)번, 나머지는 1번이어야 함
        if (values[0] == n-1 and values[1] == 1) or (values[1] == n-1 and values[0] == 1):
            return True
    
    return False


count = 0
for num in range(X, Y+1):
    if is_interesting(num):
        count += 1

print(count)